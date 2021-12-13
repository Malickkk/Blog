from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('post/<str:pk>', views.post.as_view(), name='post'),
    path('add_post', views.add_post.as_view(), name='add_post'),
]
