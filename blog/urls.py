from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:post_id>/detail', views.detail, name='detail'),
	path('<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
	path('<int:post_id>/add_like/', views.add_like, name='add_like'),
]