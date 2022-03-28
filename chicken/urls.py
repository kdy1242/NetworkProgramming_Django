from django.urls import path

from chicken import views

app_name = 'chicken'

urlpatterns = [
    path('bbq/', views.bbq, name='bbq'),
    path('goobne/', views.goobne, name='goobne'),
]