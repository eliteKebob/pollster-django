from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:todo_id>/", views.detail, name="detail"),
    path("<int:todo_id>/edit/", views.edit, name="edit"),
    path("<int:todo_id>/update/", views.update, name="update"),
    path("<int:todo_id>/delete/", views.delete, name="delete"),
]
