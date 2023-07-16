from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='details'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('create/', views.create, name='create'),
]