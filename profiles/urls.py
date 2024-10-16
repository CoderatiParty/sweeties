from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('subscription_history/<order_number>',
         views.subscription_history,
         name='subscription_history'),
    path('delete_confirmation/', views.delete_confirmation, name='delete_confirmation'),
    path('delete_profile/<int:user_id>/', views.delete_profile, name='delete_profile'),
]