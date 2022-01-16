from django.urls import path
from django.conf.urls import url
from . import views as organiser_views
from .views import (
    post_create,
    post_update,
    post_delete,
    post_detail,
    comment_delete,
    feed,
    user_profile,
    list_thread,
    thread_view,
    change_friends,
    create_message,
    user_profile_list,
)
 
 
 
urlpatterns = [      
    path('feed/', feed.as_view(), name='feed'),
    path('my-profile/', organiser_views.my_profile, name='my-profile'),
    path('profile_list/', user_profile_list.as_view(), name='user-profile-list'),
    path('feed/new/', post_create.as_view(), name='post-create'),
    path('feed/<int:pk>/update/', post_update.as_view(), name='post-update'),
    path('feed/<int:pk>/delete/', post_delete.as_view(), name='post-delete'),
    path('feed/<int:pk>/view/', post_detail.as_view(), name='post-detail'),
    path('feed/<int:post_pk>/comment/delete/<int:pk>/', comment_delete.as_view(), name='comment_delete'),
    path('profile/<int:pk>/', user_profile.as_view(), name='profile'),
    path('inbox/', list_thread.as_view(), name='inbox'),
    path('inbox/<int:pk>/', thread_view.as_view(), name='thread'),
    path('inbox/<int:pk>/create_message/', create_message.as_view(), name="create_message"),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', organiser_views.change_friends, name='change_friends'), 




 ]
 
