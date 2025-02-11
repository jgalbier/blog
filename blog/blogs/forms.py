from django import forms
from .models import Blog, BlogPost

class BlogForm(forms.ModelForm):
    """Simple form for user entry of a blog."""
    class Meta:
        model = Blog
        fields = ['text']
        labels = {'text' : ''}

class BlogPostForm(forms.ModelForm):
    """Simple form for user entry of a post for a blog."""
    class Meta:
        model = BlogPost
        fields = ['text']
        labels = {'text' : ''}
        widgets = {'text' : forms.Textarea(attrs={'cols':80})}