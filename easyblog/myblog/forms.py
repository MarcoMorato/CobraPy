from django import forms
from .models import Category


class PostForm(forms.Form):
    title = forms.CharField(max_length=100, label='Название', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={"class": "form-control",
                                                                                          "rows": 3}))
    categories = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='~Выбрать категорию~',
                                        widget=forms.Select(attrs={
                                            "class": "form-control",
                                            }))
