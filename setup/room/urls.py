from django.urls import path

from . import views

app_name = 'rooms'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultsView.as_view(), name='result'),
    path('new', views.new, name='new'),
]
