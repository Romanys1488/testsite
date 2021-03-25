from django.urls import path, include
from .views import *
from allauth.socialaccount import providers
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('colors/', colors_list, name='color_list_url'),
    path('color/<str:slug>/', ColorDetail.as_view(), name='color_detail_url'),
    path('sizes/', sizes_list, name='size_list_url'),
    path('attributesbound/', ItemAttributes.as_view(), name='bound_create_url'),
    path('attributesbound/<str:slug>/', ItemAttributes.as_view(), name='bound_detail_url'),
    path('attributes/create/', AttrsCreate.as_view(), name='attrs_create_url'),
    path('attributes/', attributes_list, name='attributes_list_url'),
    path('attributes/<str:slug>/', AttrsDetail.as_view(), name='attrs_detail_url'),
    path('attributes/<str:slug>/update/', AttrsDetail.as_view(), name='attrs_update_url'),
    path('attributes/<str:slug>/delete/', AttrsDelete.as_view(), name='attrs_delete_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.account.urls')),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
