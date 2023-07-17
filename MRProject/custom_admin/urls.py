from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    #Home
    path('', views.index, name = 'admin_home'),

    #Employee
    path('add-employee/', views.CreateEmployee.as_view(), name='add_employee'),
    path('employees/', views.ListEmployee.as_view(), name='list_employee'),
    path('update-employee/<pk>/', views.UpdateEmployee.as_view(), name='update_employee'),

    #Products
    path('products/', views.ListProducts.as_view(), name = 'admin_products'),

    #Deals
    path('deals/', views.AdminDeals.as_view(), name = 'admin_deals'),
    path('deals-details/', views.AdminDealsDetail.as_view(), name = 'admin_deals_details'),

    #VisitDetails
    path('visit-details/', views.AdminDoctorSchedule.as_view(), name = 'admin_visit_details'),

    #API Calls
    path('api/products/', views.ListProductsAPI.as_view(), name = 'products_api'),
    path('api/deals-details/', views.AdminDealsDetailAPI.as_view(), name = 'deals_details_api'),
]