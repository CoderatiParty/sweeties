from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscriptions, name='subscriptions'),
    path('<int:subscription_id>/', views.subscription, name='subscription'),
]