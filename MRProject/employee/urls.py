from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name = 'employee_home'),
    ##Authentication
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    # path('register/', views.register, name='register'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),

    ##Products
    path('product_add/', views.AddProduct.as_view(), name = 'add_product'),
    path('products/<int:page>', views.ViewProducts.as_view(), name = 'products'),

    ##Doctors
    path('doctor_add/', views.AddDoctor.as_view(), name = 'add_doctor'),
    
    #Schedule
    path('schedule_appointment', views.ScheduleAppointment.as_view(), name = 'schedule'),
    path('schedule/', views.Schedule.as_view(), name = 'today_schedule'),

    #Deals
    path('deals/', views.DealsDetailView.as_view(), name = 'deals_detail'),
]