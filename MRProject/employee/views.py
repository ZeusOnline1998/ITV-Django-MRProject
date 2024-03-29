from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, DealsDetail, Doctor, DoctorSchedule
from .forms import *
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import TemplateHTMLRenderer


# Create your views here.
# @login_required(login_url='admin/')
# class Index(View):

#     template_name = 'employee/index.html'

@login_required
def index(request):

    product_count = Product.objects.all().count()
    
    context = {
        'product_count': product_count,
    }
    return render(request, 'employee/index.html', context)


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
    success_url = reverse_lazy('products', kwargs = {"page": 1})

    def get(self, request):
        form = self.form_class(initial={'employee': request.user.first_name})
        return render(request, self.template_name, {'form': form})

    
    
class AddProductAPI(APIView):

    model = Product
    serializer_class = ProductSerializer
    template_name = 'employee/add_product.html'
    renderer_classes = [TemplateHTMLRenderer]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        serializer = ProductSerializer()
        return Response({"serializer": serializer})


    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            


class ViewProducts(ListView):

    model = Product
    template_name = "employee/products.html"
    paginate_by = 7


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
            messages.success(self.request, "Doctor information added successfully")
        else:
            messages.error(self.request, "Error Processing Data")
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
            messages.success(self.request, "Appointment Scheduled")
        else:
            messages.error(self.request, "Error Processing Data")
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
            messages.success(self.request, "Deals closed")
        else:
            messages.error(self.request, "Error Processing Data")
        return redirect('employee_home')
    

def user_login(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        # print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # print(username, password)
            user = authenticate(username=username, password=password)
            # print(user.is_staff)
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('employee_home')
                else:
                    messages.error(request, "User not allowed access here")
            else:
                messages.error(request, "User not found")
        
            
    form = AuthenticationForm()
    return render(request, 'login.html', {"form":form})