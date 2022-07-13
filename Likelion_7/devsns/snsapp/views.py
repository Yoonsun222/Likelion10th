from contextlib import redirect_stderr
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, PostForm, FreeCommentForm, FreePostForm
from .models import Post,FreePost




# Create your views here.
def home(request):
#    posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts': posts})


def postcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
   
    #request method가 post일 경우 입력 값 데이터베이스에 저장
    else:
        form = PostForm()
    
    return render(request, 'post_form.html', {'form': form})

    #request method가 get일 경우 form입력 html 띄어준다.


def detail(request, post_id):
    post_detial = get_object_or_404(Post, pk= post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail': post_detial, 'comment_form': comment_form})


def new_comment(request, post_id):
    filled_form = CommentForm(request.Post)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post =  get_object_or_404(Post, pk= post_id)
        finished_form.save()

    return redirect('detail', post_id)



def freehome(request):
    # posts = Post.objects.all()
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'free_index.html', {'freeposts': freeposts})


def freepostcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user            # user 추가!
            unfinished.save()
            return redirect('freehome')
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form})


def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form': comment_form})


def new_freecomment(request, post_id):
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)
