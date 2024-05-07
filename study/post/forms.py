from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']



# forms.py
from django import forms
from .widgets import ClearableMultipleFileInput
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'images']

    images = forms.ImageField(widget=ClearableMultipleFileInput, required=False)







        

