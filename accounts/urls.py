from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    # path('<slug:category_slug>/', store, name='products_by_category'),
    # path('<slug:category_slug>/<slug:product_slug>', product_detail, name='product_detail'),
]