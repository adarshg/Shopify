from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('lap/', views.laptop, name='lap'),
    path('lap_detail/<int:pk>', views.laptop_detail, name='lap_detail'),
    path('add_to_cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('show_cart', views.show_cart, name='show_cart'),
    path('pluscart/', views.plus_cart, name='plus_cart'),
    path('minuscart/', views.minus_cart, name='minus_cart'),
    path('removecart/', views.remove_cart, name='remove_cart'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('buynow/<int:amt>', views.buynow, name='buynow'),
    path('profile/', views.profile_user, name='profile'),
    path('order/', views.order, name='order'),
    path('success/', views.success, name='success'),

]
