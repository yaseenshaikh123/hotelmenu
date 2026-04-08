from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('save-order/', views.save_order, name='save_order'),
    path('order/<int:id>/', views.order_detail, name='order_detail'),
]

path('payment/<int:id>/', views.payment_page, name='payment'),