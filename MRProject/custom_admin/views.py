from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, View
from django.contrib.auth.models import User
from employee.models import Product, DealsDetail, Doctor, DoctorSchedule
from .forms import RegistrationForm, AdminProductForm, AdminDealsDetailForm, AdminDoctorScheduleForm
from employee.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

def index(request):

    return render(request, 'admins/index.html')


class CreateEmployee(CreateView):

    model = User
    form_class = RegistrationForm
    template_name = 'admins/add_employee.html'
    success_url = reverse_lazy('admin_home')

    
        

class ListEmployee(ListView):

    model = User
    template_name = 'admins/list_employees.html'


class ListProducts(ListView):

    model = Product
    form_class = AdminProductForm
    template_name = 'admins/list_products.html'

    def get(self, request):

        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = self.form_class(request.POST)
        products = Product.objects.filter(employee = request.POST['first_name'])
        context = {
            'form': form,
            'products': products
        }
        return render(request, self.template_name, context)

    
class AdminDealsDetail(ListView):

    model = DealsDetail
    form_class = AdminDealsDetailForm
    template_name = 'admins/deals_details.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class()
        deals = DealsDetail.objects.filter(employee = request.POST['employee']).count()
        employee = request.POST['employee']
        context = {
            'form': form,
            'deals': deals,
            'employee': employee
        }
        return render(request, self.template_name, context)

class AdminDoctorSchedule(ListView):

    model = DoctorSchedule
    form_class = AdminDoctorScheduleForm
    template_name = 'admins/doctor_visit_details.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class()
        schedule_count = DoctorSchedule.objects.filter(employee = request.POST['employee']).filter(date_of_schedule__month = request.POST['month']).count()
        employee = request.POST['employee']
        context = {
            'form': form,
            'schedule_count': schedule_count,
            'employee': employee
        }
        return render(request, self.template_name, context)