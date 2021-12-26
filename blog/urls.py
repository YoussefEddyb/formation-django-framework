from os import name
from django.urls import path
from blog.views import index, show, create, edit, delete

urlpatterns = [
    path('', index, name="list_of_articles"),
    path('create/', create, name="create_article"),
    path('<int:id>/show', show, name="show_article"),
    path('<int:id>/edit', edit, name="edit_article"),
    path('<int:id>/delete', delete, name="delete_article")
]