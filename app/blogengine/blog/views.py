from django.shortcuts import render
from django.shortcuts import redirect
from django.urls      import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import *
from .utils import *
from .forms import TagForm, PostForm, AttrsCreateForm, BoundForm, AttrsCreate

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator

from django.db.models import Q

from cart.forms import CartAddItemForm

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

class ColorDetail(ObjectDetailMixin, View):
    model = Color
    template = 'blog/color_detail.html'

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, UserPassesTestMixin, View):
    model_form = PostForm
    template   = 'blog/post_create_form.html'
    raise_exception = True

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, UserPassesTestMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True
    login_url = '/login'
    redirect_field_name = 'next'


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, UserPassesTestMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


def posts_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 4)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'blog/index.html', context=context)


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, UserPassesTestMixin, View):
    model_form = TagForm
    template   = 'blog/tag_create.html'
    raise_exception = True

class AttrsCreate(LoginRequiredMixin, ObjectCreateMixin, UserPassesTestMixin, View):
    model_form = AttrsCreate
    template   = 'blog/attributes_create_form.html'
    raise_exception = True

class ItemAttributes(LoginRequiredMixin, ObjectCreateMixin, UserPassesTestMixin, View):
    model = BoundTable
    model_form = BoundForm
    template   = 'blog/bound_item_attributes.html'
    raise_exception = True

class AttrsUpdate(LoginRequiredMixin, ObjectUpdateMixin, UserPassesTestMixin, View):
    model = AttributeType
    model_form = AttrsCreateForm
    template   = 'blog/attributes_update_form.html'
    raise_exception = True

class AttrsDelete(LoginRequiredMixin, ObjectDeleteMixin, UserPassesTestMixin, View):
    model = AttributeType
    template   = 'blog/attributes_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True

class AttrsDetail(ObjectDetailMixin, View):
    model = AttributeType
    template = 'blog/attribute_detail.html'
    raise_exception = True

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, UserPassesTestMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, UserPassesTestMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = True

class AttributeValueDetail(ObjectDetailMixin, View):
    model = ItemAttributes
    template = 'blog/post_detail.html'
    raise_exception = True

def AttributesItem(request):
    form_1 = BoundForm(request.POST)
    form_2 = AttrsCreateForm(request.POST)
    if form_1.is_valid() and form_2.is_valid():
        form_1.save()
        form_2.save()

        return redirect('/app/')


    context = {
        'form1': form_1,
        'form2': form_2
    }

    return render(request, 'blog/bound_item_attributes.html', context)

    template = 'blog/bound_item_attributes.html'
    raise_exception = True

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

def colors_list(request):
    colors = Color.objects.all()
    return render(request, 'blog/colors_list.html', context={'colors': colors})

def sizes_list(request):
    sizes = Size.objects.all()
    return render(request, 'blog/sizes_list.html', context={'sizes': sizes})

def attributes_list(request):
    attributes = AttributeType.objects.all()
    return render(request, 'blog/attribute_list.html', context={'attributes': attributes})
