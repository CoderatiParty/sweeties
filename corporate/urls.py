from django.urls import path
from . import views

urlpatterns = [
    path('', views.corporate, name='corporate'),
    path('about/', views.about, name='about'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('payments/', views.payments, name='payments'),
    path('refunds/', views.refunds, name='refunds'),
]