from django import forms
from .models import Tag, Post, Color, Size, AttributeType, ItemAttributes, BoundTable
from django.core.exceptions import ValidationError
from PIL import Image


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название товара'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ЧПУ'}),
        }


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug'+' '+'\"'+ new_slug +'\"' +' '+'is already taken.')
        return new_slug




class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = ['title', 'slug', 'body', 'tags', 'item_type', 'image', 'price', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название товара'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ЧПУ'}),
            'item_type': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Атрибут'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание предмета'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug


class BoundForm(forms.ModelForm):
    class Meta:
        model = BoundTable

        fields = ['item_id', 'attribute_id']

        widgets = {
        'item_id': forms.SelectMultiple(attrs={'class': 'form-control'}),
        'attribute_id': forms.SelectMultiple(attrs={'class': 'form-control'}),
        'value': forms.TextInput(attrs={'class': 'form-control'}),
        }



class AttrsCreateForm(forms.ModelForm):
    class Meta:
        model = ItemAttributes
        fields = ['label', 'size', 'color']
        widgets = {
        'size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Размер'}),
        'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Цвет'}),
        'label': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Производитель'}),
        }


class AttrsCreate(forms.ModelForm):
    class Meta:
        model = AttributeType
        fields = ['item_type']
        widgets = {
                'item_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Атрибут'}),
                }
