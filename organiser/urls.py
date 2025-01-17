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
    add_like,
    dislike,
    post_notification,
    follow_notification,
    thread_notification,
    remove_notification,
    event_notification,
    search_user,

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
    path('feed/<int:pk>/like/', add_like.as_view(), name='like'),
    path('feed/<int:pk>/dislike/', dislike.as_view(), name='dislike'),
    path('notification/<int:notification_pk>/post/<int:post_pk>/', post_notification.as_view(), name='post_notification'),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>/', follow_notification.as_view(), name='follow_notification'),
    path('notification/<int:notification_pk>/thread/<int:object_pk>/', thread_notification.as_view(), name='thread_notification'),
    path('notification/<int:notification_pk>/event/<int:object_pk>/', event_notification.as_view(), name='event_notification'),
    path('notification/delete/<int:notification_pk>/', remove_notification.as_view(), name='remove_notification'),
    path('search/', search_user.as_view(), name='search'),





 ]
 
