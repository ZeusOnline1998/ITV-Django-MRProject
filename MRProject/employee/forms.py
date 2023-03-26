from django import forms
from .models import Product, Doctor, DoctorSchedule, DealsDetail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'

    # name = forms.CharField(
    #     widget = forms.TextInput(attrs={
    #         'class':'form-control',
    #         'placeholder':'Enter Product Name'
    #     })
    # )
    # company = forms.CharField(
    #     widget = forms.TextInput(attrs={
    #         'class':'form-control',
    #         'placeholder':'Enter Company Name'
    #     })
    # )
    # image = forms.ImageField(
    #     required=False
    # )
    # price = forms.CharField(
    #     widget = forms.TextInput(attrs={
    #         'class':'form-control',
    #         'placeholder':'Product Price'
    #     })
    # )
    # employee = forms.CharField(
    #     widget = forms.TextInput(attrs={
    #         'class':'form-control',
            
    #     })
    # )

    


    # Design the form here if needed

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorScheduleForm(forms.ModelForm):

    class Meta:
        model = DoctorSchedule
        fields = '__all__'

class DealsDetailForm(forms.ModelForm):

    class Meta:
        model = DealsDetail
        fields = '__all__'