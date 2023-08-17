from django.urls import path

from . import views

urlpatterns = [
    path('persons/', views.list_create),
    path('persons/<int:pk>', views.retrieve_update_delete),
]
