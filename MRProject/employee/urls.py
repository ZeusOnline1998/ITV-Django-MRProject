from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name = 'employee_home'),
    ##Authentication
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    # path('register/', views.register, name='register'),
    path('logout/', auth_view.LogoutView.as_view(template_name='login.html'), name='logout'),

    ##Products
    path('product_add/', views.add_product.as_view(), name = 'add_product'),
    path('products/', views.view_products, name = 'products'),

    ##Doctors
    path('doctor_add/', views.add_doctor, name = 'add_doctor'),
    
    #Schedule
    path('schedule_appointment', views.schedule_appointment, name = 'schedule'),
    path('schedule/', views.schedule, name = 'today_schedule'),

    #Deals
    path('deals/', views.deals_detail, name = 'deals_detail'),
]