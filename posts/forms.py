from django import forms

from .models import Posts


class blogForm(forms.Form):
    title = forms.CharField(label='title', max_length=200)
    author = forms.ChoiceField()
    body = forms.CharField(label='body', max_length=10000000)


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'author', 'body')
        widget = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter the title of the post',
                'class': 'form-control'
                }), 
            'body': forms.TextInput(attrs={
                'placeholder': 'Enter the content of the post',
                'class': 'form-control'
                }),
        }

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'author': forms.ModelChoiceField(queryset=Posts.objects.filter()),
        #     'body': forms.Textarea(attrs={'class': 'form-control'}),
        # }
        def __init__(self, author, *args, **kwargs):
            self.fields['author'].queryset = Posts.objects.filter(
                author=author)
