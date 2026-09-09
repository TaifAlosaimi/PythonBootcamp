from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


def feed(request):
    posts = Post.objects.all().order_by("-id")

    context = {
        "posts": posts,
    }

    return render(request, "feed/feed.html", context)


def create_post(request):

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("feed:feed")

    else:
        form = PostForm()

    context = {
        "form": form,
    }

    return render(request, "feed/create_post.html", context)


def like_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.likes += 1
        post.save()

    return redirect("feed:feed")