from django.shortcuts import render

from .forms import PostForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def postcreate(request):
    if request.method == 'POST':
        pass
    #request method가 post일 경우 입력 값 데이터베이스에 저장
    else:
        form = PostForm()
    
    return render(request, 'post_form.html', {'form': form})

    #request method가 get일 경우 form입력 html 띄어준다.