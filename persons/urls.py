from django.urls import path

from . import views

urlpatterns = [
    path('persons/', views.PersonListCreateAPIView.as_view()),
    path('persons/<int:pk>', views.PersonRetrieveUpdateDeleteAPIView.as_view()),
]
