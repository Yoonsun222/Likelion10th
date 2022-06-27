from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

# Create your views here.
def home(request):
    #블로그 글을 모두 띄우는 코드
    #posts = Blog.objects.all()
    posts= Blog.objects.filter().order_by('-date')
    return render(request ,'index.html', {'posts': posts})

#블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')


#블로그 글을 저장해주는 함수
def create(request):
    #request의 method가 post면 블로그 객체를 생성해서 데이터 베이스에다가 저장
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home') #정상적으로 끝났으면 home으로 다시 돌아가라



#django form을 이용해서 입력 값을 받는 함수
# get(=입력값을 받을 수 있는  html을 갖다 줘) 과 post(=입력한 내용을  데이터 베이스에 저장. form에서 입력한 내용을 처리) 둘 다 처리 가능한 함수
def formcreate(request):
    if request.method == 'POST':
        #입력 내용 DB에 저장
        form = BlogForm(request.POST)
        if form.is_valid():
            #저장해라
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.date = timezone.now()
            post.save()
            return redirect('home')
    else:
        #입력을 받을 수 있는 html 갖다 주기
        form = BlogForm()

    #세번째 인자로 views.pyㅐ의 데이터를 html에 넘겨줄 수 있는데 단, 딕셔너리 자료형으로 넘겨주어야한다.
    return render(request, 'form_create.html', {'form':form})

def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        #입력 내용 DB에 저장
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            #저장해라
            form.save()
            return redirect('home')
    else:
        #입력을 받을 수 있는 html 갖다 주기
        form = BlogModelForm()

    #세번째 인자로 views.pyㅐ의 데이터를 html에 넘겨줄 수 있는데 단, 딕셔너리 자료형으로 넘겨주어야한다.
    return render(request, 'form_create.html', {'form':form})
    


#pk값을 이용해 특정 모델 객체 하나만 갖고오는 코드 : get_object_or_404(모델, 어떤 객체를 가져 오는지)
def detail(request, blog_id):
    #blog_id 번째 블로그 글을 데이터베이스로부터 갖고 와서 
    blog_detail = get_object_or_404(Blog, pk=blog_id)    
    #blog_id 번째 블로그 글을 detail.html로 띄워주는 코드
    return render(request, 'detail.html', {'blog_detail': blog_detail})