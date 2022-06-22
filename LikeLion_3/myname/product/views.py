from urllib import request
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'productmain.html')