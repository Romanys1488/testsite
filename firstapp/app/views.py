from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Item, Tag
from .utils import *
from .forms import TagForm, PostForm

def items_list(request):
    items = Item.objects.all()
    return render(request, 'app/index.html', context={'items': items})

class ItemDetail(ObjectDetailMixin, View):
    model = Item
    template = 'app/item_detail.html'

class ItemCreate(ObjectCreate, View):
    form_model = PostForm
    template = 'app/item_create_form.html'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'app/tag_detail.html'

class TagCreate(ObjectCreate, View):
    form_model = TagForm
    template = 'app/tag_create.html'

class TagUpdate(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(instance=tag)
        return render(request, 'app/tag_update_form.html', context={'form': bound_form, 'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(request.POST, instance=tag)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'app/tag_update_form', context={'form': bound_form, 'tag': tag})   

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'app/tags_list.html', context={'tags': tags})
