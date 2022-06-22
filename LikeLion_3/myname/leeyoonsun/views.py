from django.shortcuts import render

# Create your views here.

def birth(request):
    return render(request, "birth.html")

def mynameis(request):
    return render(request, "myname.html")