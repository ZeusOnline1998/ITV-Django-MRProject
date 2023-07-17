from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, View, UpdateView
from django.contrib.auth.models import User
from employee.models import Product, DealsDetail, Doctor, DoctorSchedule
from .forms import RegistrationForm, AdminProductForm, AdminDealsDetailForm, AdminDoctorScheduleForm
from employee.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from rest_framework.views import APIView
from employee.serializers import *
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
# Create your views here.

@login_required
def index(request):

    if request.user.is_superuser:
        employee_count = User.objects.all().count()
        
        return render(request, 'admins/index.html', {'employee_count': employee_count})
    else:
        messages.error(request, "Only admins can access the admin dashboard")
        return redirect('employee_home')


class CreateEmployee(CreateView):

    model = User
    form_class = RegistrationForm
    template_name = 'admins/add_employee.html'
    success_url = reverse_lazy('admin_home')

    
        

class ListEmployee(ListView):

    model = User
    template_name = 'admins/list_employees.html'


class UpdateEmployee(UpdateView):

    model = User
    template_name = 'admins/update_employee.html'

    fields = ['username', 'first_name', 'last_name', 'email', 'is_staff']

    success_url = reverse_lazy('list_employee')

class ListProducts(ListView):

    model = Product
    form_class = AdminProductForm
    template_name = 'admins/list_products.html'

    def get(self, request):

        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    # def post(self, request):

    #     form = self.form_class(request.POST)
    #     products = Product.objects.filter(employee = request.POST['first_name'])
    #     form = self.form_class()
    #     context = {
    #         'form': form,
    #         'products': products
    #     }
    #     return render(request, self.template_name, context)


class ListProductsAPI(APIView):

    model = Product
    serializer_class = ProductSerializer
    

    def get(self, request):
        first_name = request.GET.get('first_name')
        queryset = Product.objects.filter(employee = first_name)
        return Response(queryset.values())

    
class AdminDeals(ListView):

    model = DealsDetail
    form_class = AdminDealsDetailForm
    template_name = 'admins/deals.html'

    def get(self, request):
        form = self.form_class()
        deals = DealsDetail.objects.all().values('employee').annotate(total=Count('employee')).order_by('-total')
        # employee = request.POST['employee']
        context = {
            'form': form,
            'deals': deals,
            # 'employee': employee
        }
        return render(request, self.template_name, context)

    # def post(self, request):
    #     form = self.form_class()
    #     deals = DealsDetail.objects.all().values('employee').annotate(total=Count('employee'))
    #     employee = request.POST['employee']
    #     context = {
    #         'form': form,
    #         'deals': deals,
    #         # 'employee': employee
    #     }
    #     return render(request, self.template_name, context)


class AdminDealsDetail(ListView):

    model = DealsDetail
    form_class = AdminDealsDetailForm
    template_name = 'admins/deals_details.html'

    def get(self, request):

        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = self.form_class()
        deals = DealsDetail.objects.filter(employee = request.POST['employee'])
        context = {
            'form': form,
            'deals': deals
        }
        return render(request, self.template_name, context)

class AdminDealsDetailAPI(APIView):

    model = DealsDetail
    serializer_class = DealsDetailSerializer

    def get(self, request):

        queryset = DealsDetail.objects.filter(employee = request.GET.get('employee'))
        return Response(queryset.values())


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