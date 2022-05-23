from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_posts, name='posts'),
    path('create-post/', views.create_post, name='create-post'),
    path('update-post/<int:p_id>/', views.update_post, name="update_post"),
    path('delete-post/<int:p_id>/', views.delete_post, name="delete_post")
]