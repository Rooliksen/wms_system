# Определяет схемы URL для галереи

from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    # Страница со списком всех фотографий
    path('main/', views.main, name='main'),
    path('photo/<str:pk>/', views.view_photo, name='photo'),
    path('add/', views.add_photo, name='add'),
]