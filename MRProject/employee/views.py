from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, DealsDetail, Doctor, DoctorSchedule
from .forms import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.
# @login_required(login_url='admin/')
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

class add_product(CreateView):

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


def view_products(request):

    return render(request, 'employee/products.html')


def add_doctor(request):

    return render(request, 'employee/add_doctor.html')


def schedule_appointment(request):

    return render(request, 'employee/schedule_appointment.html')


def schedule(request):

    return render(request, 'employee/schedule.html')


def deals_detail(request):

    return render(request, 'employee/deals_detail.html')