from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('subscription_history/<subscription_number>',
         views.subscription_history,
         name='subscription_history'),
]