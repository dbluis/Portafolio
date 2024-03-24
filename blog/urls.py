from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.render_post, name="posts"),
    path("<int:post_id>", views.post_detail, name="post_detail"),
    path("create_post", views.create_post, name="create_post"),
    path('<int:post_id>/edit/', views.post_update, name='post_update'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
]
