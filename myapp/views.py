from django.shortcuts import render
from .models import *
from .form import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def home(request):

    p = Paginator(Post.objects.all().order_by("?"), 6)
    page = request.GET.get("page")
    posts = p.get_page(page)

    context = {
        "posts": posts,
    }
    return render(request, "home.html", context)


def PostSearch(request):
    if request.method == "POST":
        blog_name = request.POST["search-element"]
        print(blog_name)
        posts = Post.objects.filter(Title=blog_name)
        if not posts.exists():
            messages.error(request, f"There are no posts with the title '{blog_name}'")

    context = {
        "posts": posts,
    }
    return render(request, "searchpost.html", context)

@login_required(login_url="login")
def posting(request):
    form = PostFrom()
    if request.method == "POST":
        form = PostFrom(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Author = request.user
            instance.save()
            return redirect("home")

    else:
        form = PostFrom()

    return render(request, "newpost.html", {"form": form})


@login_required(login_url="login")
def post_detail(request, slug):

    post = Post.objects.get(slug=slug)
    comment = Comment.objects.filter(Post=post)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Post = post
            instance.Author = request.user
            instance.save()
            return redirect("post", post.slug)

    else:
        form = CommentForm()

    context = {"posts": post, "form": form, "comment": comment}
    return render(request, "post.html", context)


@login_required(login_url="login")
def profile(request, pk):
    user = CustomUser.objects.get(id=pk)
    post = Post.objects.filter(Author=pk)
    context = {"posts": post, "users": user, "user_profile_details": user}
    return render(request, "profile.html", context)
