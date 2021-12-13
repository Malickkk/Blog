from django import forms

from .models import Posts


class blogForm(forms.Form):
    title = forms.CharField(label='title', max_length=200)
    body = forms.CharField(label='body', max_length=10000000)


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
