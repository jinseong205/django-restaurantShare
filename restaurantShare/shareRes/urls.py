from urllib.parse import urlparse
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail/', views.restaurantDetail, name='resDetatilPage'),
    path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'),
    path('categoryCreate/', views.categoryCreate, name='cateCreatePage'),
    path('categoryCreate/create', views.Create_category, name='cateCreate'),
    
]