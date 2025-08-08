from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from common.utils import get_profile
from posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from posts.models import Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form: PostCreateForm):
        form.instance.author = get_profile()
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/details-post.html'


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    pk_url_kwarg = 'post_id'
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dashboard')


class PostDeleteView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    pk_url_kwarg = 'post_id'
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs


    # option 2:
    # def get_initial(self) -> dict:   # fill the form with data
    #     return self.object.__dict__

    # def form_invalid(self, form: PostDeleteForm):  # no validation of the form, when delete
    #     return self.form_valid(form)

