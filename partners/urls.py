from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('partners/', views.partner_list, name='partner_list'),
    path('partners/add/', views.add_partner, name='add_partner'),
    path('partners/<int:pk>/', views.partner_detail, name='partner_detail'),
    path('partners/<int:pk>/edit/', views.edit_partner, name='edit_partner'),
]