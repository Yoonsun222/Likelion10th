from django.shortcuts import render, redirect, get_object_or_404
from .forms import BoardModelForm
from .models import Board
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