from django import forms
from .models import Blog

class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget = forms.Textarea) #조금 더 넓은 문자열로 입력 받을거얏


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        #fields = '__all__'
        fields = ['title', 'body']