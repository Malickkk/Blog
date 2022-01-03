from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:id>', views.post, name='post'),
    path('add_post', views.add_post, name='add_post'),
    path('delete_post/<str:id>', views.delete_post, name='delete_post'),
    path('update_post/<str:id>', views.update_post, name='update_post')
]
