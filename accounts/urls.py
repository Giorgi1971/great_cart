from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate')

    # path('<slug:category_slug>/', store, name='products_by_category'),
    # path('<slug:category_slug>/<slug:product_slug>', product_detail, name='product_detail'),
]