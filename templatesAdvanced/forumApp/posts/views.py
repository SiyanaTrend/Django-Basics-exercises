from django.db.models import Q

from django.shortcuts import render, redirect
from posts.forms import PostCreateForm, PostEditForm, PostDeleteForm, SearchForm
from posts.models import Post


def index(request):
    return render(request, 'common/base.html')

# use with PostForm from the forms.py:
# def index(request):
#     form = PostForm(request.POST or None)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'index.html', context)


# use with examples from the forms.py:
# def index(request):
#     form = MyFrom(request.POST or None)
#
#     # # equals:
#     # if request.method == 'GET':
#     #     form = MyFrom()
#     # else:
#     #     form = MyFrom(request.POST)
#
#     if form.is_valid():
#         print('The data is', request.POST.get('my_text'))
#         print('The data is', form.cleaned_data.get('my_text'))
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'index.html', context)


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
    form = PostCreateForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'posts/add-post.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostEditForm(request.POST or None, instance=post)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'posts/edit-post.html', context)


def post_details(request, pk: int):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post,
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