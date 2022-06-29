from django.shortcuts import render, redirect, get_object_or_404
from .forms import BoardModelForm
from .models import Board, Comment
from django.utils import timezone

# Create your views here.
def home(request):
    posts = Board.objects.all()
    return render(request, "index.html", {'posts': posts})

def new(request):
    return render(request, "new.html")

def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        post = Board()
        post.title = request.POST['title']
        post.photo = request.FILES['photo']
        post.content = request.POST['content']
        post.date = timezone.now()
        post.save()
    
    return redirect('home')
       
def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board_detail': board_detail})


def create_comment(request, board_id):
    comments = Comment()
    if request.method == 'POST':
        comments.comment = request.POST['comment']
        comments.date = timezone.now()
        comments.post = get_object_or_404(Board, pk=board_id) #어떤 게시물에 달린 댓글인지 블로그값에다가 pk값이 id인걸로 담아줌
        comments.save()
    #대기 후 어떤 블로그 글에 담을 객체인지 post한 다음에 save해라
    return redirect('detail', board_id)