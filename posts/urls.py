from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('post/<str:pk>', views.post.as_view(), name='post'),
    path('add_post', views.add_post.as_view(), name='add_post'),
    path('delete_post/<str:pk>', views.delete_post.as_view(), name='delete_post'),
    path('update_post/<str:pk>', views.update_post.as_view(), name='update_post')
]
