from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_cart, name='cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_auto_renew/<int:item_id>/', views.update_auto_renew, name='update_auto_renew'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
]