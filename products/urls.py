# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/detail', views.product_detail, name='product_detail'),
    path('new', views.new, name='product_new'),
]
