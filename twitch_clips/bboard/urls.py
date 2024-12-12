from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('addpage/', addpage, name='addpage'),
    path('post/<str:slug>', show_post, name='post'),
    path('delete/<str:slug>', delete_page, name='delete'),
    path('streamer/<int:user_id>', show_streamer, name='streamer'),
    path('streamers/', show_streamers, name='streamers')
]

