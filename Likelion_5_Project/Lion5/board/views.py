from django.shortcuts import render, redirect
from .models import Board
from django.utils import timezone

# Create your views here.
def home(request):
    posts = Board.objects.all()
    return render(request, "index.html", {'posts': posts})

def new(request):
    return render(request, "new.html")

def create(request):
    if(request.method == 'POST'):
        post = Board()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.date = timezone.now()
        post.save()
    return redirect('home')