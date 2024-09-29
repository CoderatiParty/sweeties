from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscriptions, name='subscriptions'),
    path('add_subscription/<int:subscription_id>/', views.add_subscription, name='add_subscription'),
]