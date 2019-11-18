from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect


def post_list(request):
	posts = Post.objects.all()
	#posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'habr/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'habr/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'habr/post_edit.html', {'form': form})

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'habr/post_edit.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('/')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request = request, template_name = "registration/register.html", context={"form":form})

        form = UserCreationForm
        return render(request = request, template_name = "registration/register.html", context={"form":form})