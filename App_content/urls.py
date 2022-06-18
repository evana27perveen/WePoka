from django.urls import path
from . import views

app_name = 'App_content'

urlpatterns = [
    path('', views.new_podcast, name='new_podcast'),
    path('pod-showcase/', views.podcast_listview, name='pod-showcase'),
    path('new-post/', views.new_post, name='new-post'),
    path('post-listview/', views.post_listview, name='post-listview'),
    path('post-react/<int:pk>/', views.post_react, name='post-react'),
]
