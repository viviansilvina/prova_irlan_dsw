from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("modalidade/<int:id>/", views.modalidade),
    path("equipe/<int:id>/", views.equipe)
]