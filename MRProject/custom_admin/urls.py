from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    #Home
    path('', views.index, name = 'admin_home'),

    #Employee
    path('add-employee/', views.CreateEmployee.as_view(), name='add_employee'),
    path('employees/', views.ListEmployee.as_view(), name='list_employee'),

    #Products
    path('products/', views.ListProducts.as_view(), name = 'admin_products'),

    #Deals
    path('deals/', views.AdminDealsDetail.as_view(), name = 'admin_deals'),

    #VisitDetails
    path('visit-details/', views.AdminDoctorSchedule.as_view(), name = 'admin_visit_details'),
]