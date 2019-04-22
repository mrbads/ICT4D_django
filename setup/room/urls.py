from django.urls import path

from . import views

app_name = 'rooms'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:room_id>/', views.detail, name='detail'),
    path('<int:room_id>/result/', views.result, name='result'),
    path('<int:room_id>/input/', views.input, name='input'),
]
