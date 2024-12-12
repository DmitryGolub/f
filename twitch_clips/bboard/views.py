from django.db.models import Count
from django.shortcuts import render, redirect
from .models import Post, Streamer
from .forms import PostForm
from .utils import get_data_clip, get_data_user


def index(request):
    posts = Post.objects.all().select_related('streamer')
    context = {
        "posts": posts,
        "title": "Home page",
    }
    return render(request, 'bboard/posts.html', context)


def show_post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'title': post.title,
        'post': post,
    }
    return render(request, 'bboard/post.html', context)


def show_streamers(request):
    streamers = Streamer.objects.annotate(num_posts=Count('post')).order_by('-num_posts')

    context = {
        'title': f'Стримеры',
        'streamers': streamers,
    }
    return render(request, 'bboard/streamers.html', context)


def show_streamer(request, user_id):
    streamer = Streamer.objects.get(user_id=user_id)
    posts = Post.objects.filter(streamer=streamer)
    context = {
        'title': f'Стример - {streamer.user_name}',
        'posts': posts,
        'streamer': streamer
    }
    return render(request, 'bboard/posts.html', context)


def addpage(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            slug, title, url, image, embed, streamer_name, streamer_id = get_data_clip(**form.cleaned_data)
            author = request.user
            streamer = Streamer.objects.filter(user_id=streamer_id)
            if not streamer:
                logo = get_data_user(streamer_id)
                streamer = Streamer.objects.create(user_id=streamer_id, user_name=streamer_name, logo=logo)
            streamer = Streamer.objects.get(user_id=streamer_id)
            Post.objects.create(slug=slug, title=title, url=url,
                                image=image, embed=embed, streamer=streamer, author=author)

            return redirect("home")
    else:
        form = PostForm()
    context = {
        "title": "Добавление поста",
        "form": form,
    }
    return render(request, 'bboard/addpage.html', context)


def delete_page(request, slug):
    Post.objects.get(slug=slug).delete()
    return redirect('home')
