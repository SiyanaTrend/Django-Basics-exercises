from datetime import datetime

from django.db.models import Q
from django.forms import modelform_factory
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import classonlymethod, method_decorator
from django.views import View
from django.views.generic import TemplateView, RedirectView, CreateView, UpdateView, DeleteView, FormView, DetailView, \
    ListView
from django.views.generic.edit import FormMixin

from posts.decorators import measure_execution_time
from posts.forms import PostCreateForm, PostDeleteForm, SearchForm, CommentFrom, CommentFromSet, PostEditForm
from posts.mixins import TimeRestrictedMixin
from posts.models import Post

'''example 1'''
# def index(request):
#     return render(request, 'common/base.html')
#
'''def index(request):.... is the same as follow, using CBV:'''


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'common/base.html')


''' example 2 -> rewriting the dispatch method - check if you are log in'''
# class IndexView(View):
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return super().dispatch(request, *args, **kwargs)
#         return HttpResponse('403 Forbidden')
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'common/base.html')


'''Example 3 -> simple example of Django under the hood'''
# class MyView:
#     def dispatch(self, request, *args, **kwargs):
#         if request.method == 'GET':
#             return self.get(request, *args, **kwargs)
#     @classonlymethod
#     def as_view(cls):
#         def view(request, *args, **kwargs):
#             self = cls()
#             return self.dispatch(request, args, kwargs)
#
#         return view
#
#
# class IndexView(MyView):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'common/base.html')


'''example 4 -> static way to render template'''
# class IndexView(TemplateView):
#     template_name = 'common/base.html'


'''example 5 -> dynamic way to render template: if the first one not exists, return the next one'''
# class IndexView(TemplateView):
#      def get_template_names(self):
#         return ['other.html', 'common/base.html']


'''Example 6 -> dynamic way to render template'''
# class IndexView(TemplateView):
#     def get_template_names(self):
#         if self.request.user.is_superuser:
#             return ['common/base.html']
#
#         return ['posts/dashboard.html']

'''Example 7 -> static way to render template: 
get the current time, when start the project and never changes even if the page is refreshed '''
# class IndexView(TemplateView):
#     extra_context = {
#         'current_time': datetime.now(),
#     }
#     def get_template_names(self):
#         return ['index.html']


'''Example 8 -> static way to render template: 
get the current time, every time when the page is refreshed'''
# class IndexView(TemplateView):
#     def get_context_data(self, **kwargs):
#         super().get_context_data(**kwargs)
#         kwargs.update({
#             'current_time': datetime.now(),
#         })
#         return kwargs
#
#     def get_template_names(self):
#         return ['index.html']

'''Example 9 -> static ways to redirect to dashboard when http://localhost:8000/redirect/'''
# class MyRedirectView(RedirectView):
# url = 'http://localhost:8000/dashboard/'
# or
# pattern_name = 'index'


'''Example 10 -> dynamic way to redirect to dashboard when http://localhost:8000/redirect/'''
# class MyRedirectView(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         return reverse('dashboard')


'''Example 11 -> dynamic way to redirect to dashboard when http://localhost:8000/redirect/ 
with 'Django' word in the search bar'''

class MyRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('dashboard') + '?query=Django'


'''Example - dynamic way for dashboard/search bar functionality and  with CBV - ListView'''

@method_decorator(name='dispatch', decorator=measure_execution_time)
class Dashboard(ListView):
    model = Post
    template_name = "posts/dashboard.html"
    paginate_by = 3   # 3 posts on single page -> ...dashboard/?page=1 (2,3...pages). See dashboard.html <div class="pagination">
    query_param = "query"
    form_class = SearchForm

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs.update({
            "search_form": self.form_class(),
            "query": self.request.GET.get(self.query_param, ''),  # show the search word for ex. django -> ...dashboard/?query=django
        })
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        queryset = self.model.objects.all()
        search_value = self.request.GET.get(self.query_param)

        if search_value:
            queryset = queryset.filter(
                Q(title__icontains=search_value)
                    |
                Q(content__icontains=search_value)
                    |
                Q(author__icontains=search_value)
            )

        return queryset



'''instead of:'''
# def dashboard(request):
#     search_form = SearchForm(request.GET)
#     posts = Post.objects.all()
#
#     if request.method == "GET" and search_form.is_valid():
#         query = search_form.cleaned_data.get('query')
#         posts = posts.filter(
#             Q(title__icontains=query)
#             |
#             Q(content__icontains=query)
#             |
#             Q(author__icontains=query)
#         )
#
#     context = {
#         "posts": posts,
#         "search_form": search_form,
#     }
#
#     return render(request, 'posts/dashboard.html', context)


'''Example - static way to add post with CBV - CreateView'''

class CreatePost(TimeRestrictedMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('dashboard')
    template_name = 'posts/add-post.html'


'''instead of: '''
# def add_post(request):
#     form = PostCreateForm(request.POST or None, request.FILES or None)
#
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return redirect('dashboard')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'posts/add-post.html', context)


'''Example - dynamic way to edit post with CBV - UpdateView'''

class EditPost(TimeRestrictedMixin, UpdateView):
    model = Post
    # form_class = PostEditForm
    success_url = reverse_lazy('dashboard')
    template_name = 'posts/edit-post.html'

    """editing all fields, when admin is log in or only one field 'content' when you are the user"""

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields='__all__')
        else:
            return modelform_factory(Post, fields=('content',))


'''instead of: '''
# def edit_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#
#     """editing all fields from, when admin is log in or only one field 'content' when you are the user"""

#     if request.user.is_superuser:
#         PostEditForm = modelform_factory(Post, fields='__all__')
#     else:
#         PostEditForm = modelform_factory(Post, fields=('content',))
#
#     form = PostEditForm(request.POST or None, instance=post)
#
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return redirect('dashboard')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'posts/edit-post.html', context)


'''Example - dynamic way for comment functionality in post with CBV - DetailView'''

# class PostDetails(DetailView):
#     model = Post
#     template_name = 'posts/post-details.html'  # Not needed if named as Django expects -> post_detail.html
#
#     def get_success_url(self):
#         return reverse_lazy('post-details', pk=self.kwargs.get(self.pk_url_kwarg))
#
#     def get_form_class(self):
#         return CommentFromSet
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         comment_form_set = self.get_form_class()(request.POST)
#
#         if comment_form_set.is_valid():
#             for form in comment_form_set:
#                 comment = form.save(commit=False)  # get the comment without saving it in the database, because there are more fields in the Comment model(it is not ForeignKey)
#                 comment.author = request.user.username
#                 comment.post = self.object  # get the post, which is ForeignKey
#                 comment.save()  # when we get the author and the post we save the comment in the database
#                 return redirect(self.get_success_url())

'''Second solution for dynamic way for comment functionality in the post with CBV - DetailView'''
class PostDetails(DetailView, FormMixin):
    model = Post
    template_name = 'posts/post-details.html'  # Not needed if named as Django expects -> post_detail.html
    form_class = CommentFromSet

    def get_context_data(self, **kwargs):
        kwargs.update({
            "formset": self.get_form_class()(),
        })
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy('post-details', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form_set = self.get_form_class()(request.POST)

        if comment_form_set.is_valid():
            for form in comment_form_set:
                comment = form.save(commit=False)  # get the comment without saving it in the database, because there are more fields in the Comment model(it is not ForeignKey)
                comment.author = request.user.username
                comment.post = self.object  # get the post, which is ForeignKey
                comment.save()  # when we get the author and the post we save the comment in the database

            return self.form_valid(comment_form_set)


'''instead of: '''
# def post_details(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     comment_form_set = CommentFromSet(request.POST or None)
#
#     if request.method == "POST" and comment_form_set.is_valid():
#         for form in comment_form_set:
#             comment = form.save(commit=False)   # get the comment without saving it in the database, because there are more fields in the Comment model(it is not ForeignKey)
#             comment.author = request.user.username
#             comment.post = post  # get the post, which is ForeignKey
#             comment.save()  # when we get the author and the post we save the comment in the database
#             return redirect('post-details', pk=post.pk)
#
#     context = {
#         "post": post,
#         "formset": comment_form_set,
#     }
#
#     return render(request, 'posts/post-details.html', context)


'''Example - dynamic way to delete post with CBV - DeleteView,
returning the form with the info in it, before deleting'''

class DeletePost(DeleteView, FormView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = self.model.objects.get(pk=pk)
        return post.__dict__


'''instead of: '''
# def delete_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     form = PostDeleteForm(instance=post)
#
#     if request.method == "POST":
#         post.delete()
#         return redirect('dashboard')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'posts/delete-post.html', context)
