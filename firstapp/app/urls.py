from django.urls import path
from .views import *

urlpatterns = [
    path('', items_list, name='items_list_url'),
    path('item/create/', ItemCreate.as_view(), name='post_create_url'),
    path('item/<str:slug>/', ItemDetail.as_view(), name='item_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name = 'tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
]
