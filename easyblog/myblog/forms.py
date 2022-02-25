from django import forms
from .models import Category, Post


# class PostForm(forms.Form):
#     title = forms.CharField(max_length=100, label='Название', widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={"class": "form-control",
#                                                                                           "rows": 3}))
#     categories = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='~Выбрать категорию~',
#                                         widget=forms.Select(attrs={
#                                             "class": "form-control",
#                                             }))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'content', 'categories', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
