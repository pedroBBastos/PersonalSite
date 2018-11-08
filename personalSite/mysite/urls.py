from django.urls import path

from . import views

app_name = 'mysite'
urlpatterns = [
    path('', views.index, name='home'),
    path('unicamp/', views.unicamp, name='unicamp'),
]
