from tkinter import filedialog
from xml.etree.ElementTree import Comment
from django import forms
from .models import Post, Comments ,FreeComments,FreePost


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']




class FreePostForm(forms.ModelForm):
    class Meta:
        model = FreePost
        fields = '__all__'

class FreeCommentForm(forms.ModelForm):
    class Meta:
        model = FreeComments
        fields = ['comment']