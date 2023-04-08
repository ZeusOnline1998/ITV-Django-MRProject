from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, DealsDetail, Doctor, DoctorSchedule
from .forms import *
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.
# @login_required(login_url='admin/')
# class Index(View):

#     template_name = 'employee/index.html'

@login_required
def index(request):

    return render(request, 'employee/index.html')


# def add_product(request):

#     if request.method == 'POST':

#         product = ProductForm(data=request.POST, files=request.FILES)

#         if product.is_valid():
#            # product_data = product.save(commit=False)
#             product.save()
#             print("Entered Successfully")
            
#             return redirect('employee_home')
        
#     else:

#         product = ProductForm(initial={'employee': request.user.first_name})

#     return render(request, 'employee/add_product.html', {'form' : product})

class AddProduct(CreateView):

    model = Product
    form_class = ProductForm       
    template_name = 'employee/add_product.html'
    success_url = reverse_lazy('employee_home')

    def get(self, request):
        form = self.form_class(initial={'employee': request.user.first_name})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data = request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error Processing Data")
        return redirect('employee_home')


class ViewProducts(ListView):

    model = Product
    template_name = "employee/products.html"


class AddDoctor(CreateView):

    model = Doctor
    form_class = DoctorForm       
    template_name = 'employee/add_doctor.html'
    success_url = reverse_lazy('employee_home')

    def get(self, request):
        form = self.form_class(initial={'employee': request.user.first_name})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data = request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error Processing Data")
        return redirect('employee_home')


class ScheduleAppointment(CreateView):

    model = DoctorSchedule
    form_class = DoctorScheduleForm       
    template_name = 'employee/schedule_appointment.html'
    success_url = reverse_lazy('employee_home')

    def get(self, request):
        form = self.form_class(initial={'employee': request.user.first_name})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data = request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error Processing Data")
        return redirect('employee_home')


class Schedule(ListView):

    model = DoctorSchedule
    template_name = 'employee/schedule.html'

    def post(self, request):

        today = DoctorSchedule.objects.filter(date_of_schedule=request.POST['schedule_date']).order_by('time_of_schedule')

        return render(request, self.template_name, {'context' : today})


class DealsDetailView(CreateView):

    model = DealsDetail
    form_class = DealsDetailForm       
    template_name = 'employee/deals_detail.html'
    success_url = reverse_lazy('employee_home')

    def get(self, request):
        form = self.form_class(initial={'employee': request.user.first_name})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data = request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error Processing Data")
        return redirect('employee_home')