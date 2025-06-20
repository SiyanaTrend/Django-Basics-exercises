from django.db.models import Q
from django.forms import modelform_factory
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.utils.decorators import classonlymethod
from django.views import View

from posts.forms import PostCreateForm, PostDeleteForm, SearchForm, CommentFrom, CommentFromSet
from posts.models import Post


'''example 1'''
# def index(request):
#     return render(request, 'common/base.html')
#
'''def index(request):.... is the same as follow, using CBV:'''

# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'common/base.html')


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
#             return self.dispach(request, args, kwargs)
#
#         return view
#
#
# class IndexView(MyView):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'common/base.html')



def dashboard(request):
    search_form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == "GET" and search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        posts = posts.filter(
            Q(title__icontains=query)
                |
            Q(content__icontains=query)
                |
            Q(author__icontains=query)
        )

    context = {
        "posts": posts,
        "search_form": search_form,
    }

    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    form = PostCreateForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'posts/add-post.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    """editing all fields from admin, when log in or only one field 'content' when you are the user"""
    if request.user.is_superuser:
        PostEditForm = modelform_factory(Post, fields='__all__')
    else:
        PostEditForm = modelform_factory(Post, fields=('content',))

    form = PostEditForm(request.POST or None, instance=post)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'posts/edit-post.html', context)


""" Example 1 - use with example 1 in post-details.html"""
# def post_details(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     comment_form = CommentFrom(request.POST or None)
#
#     if request.method == "POST" and comment_form.is_valid():
#         comment = comment_form.save(commit=False)   # get the comment without saving it in the database, because there are more fields in the Comment model
#         comment.author = request.user.username
#         comment.post = post
#         comment.save()  # when we get the author and the post we save the comment in the database
#
#     context = {
#         "post": post,
#         "comment_form": comment_form,
#     }
#
#     return render(request, 'posts/post-details.html', context)


def post_details(request, pk: int):
    post = Post.objects.get(pk=pk)
    comment_form_set = CommentFromSet(request.POST or None)

    if request.method == "POST" and comment_form_set.is_valid():
        for form in comment_form_set:
            comment = form.save(commit=False)   # get the comment without saving it in the database, because there are more fields in the Comment model(it is not ForeignKey)
            comment.author = request.user.username
            comment.post = post  # get the post, which is ForeignKey
            comment.save()  # when we get the author and the post we save the comment in the database
            return redirect('post-details', pk=post.pk)

    context = {
        "post": post,
        "formset": comment_form_set,
    }

    return render(request, 'posts/post-details.html', context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == "POST":
        post.delete()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'posts/delete-post.html', context)
