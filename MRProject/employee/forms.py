from django import forms
from .models import Product, Doctor, DoctorSchedule, DealsDetail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'

    name = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Product Name'
        })
    )
    company = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Company Name'
        })
    )
    image = forms.ImageField(
        required=False
    )
    price = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Product Price'
        })
    )
    employee = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'disabled' : 'true',
        })
    )

    


    # Design the form here if needed

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'

    name = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Doctor\'s Name'
        })
    )
    
    specialisation = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Chest, Heart, General, Orthopaedic, etc'
        })
    )
    
    contact_number = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Doctor\'s Contact Number'
        })
    )
    
    location = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Doctor\'s Location'
        })
    )
    
    employee = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'disabled' : 'true'
        })
    )
    
    

class DoctorScheduleForm(forms.ModelForm):

    class Meta:
        model = DoctorSchedule
        fields = '__all__'

    name = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Doctor\'s Name'
        })
    )

    date_of_schedule = forms.DateField(
        widget = forms.DateInput()
    )

    time_of_schedule = forms.TimeField(
        widget = forms.TimeInput()
    )

    employee = forms.CharField(
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'disabled' : 'true'
        })
    )

class DealsDetailForm(forms.ModelForm):

    class Meta:
        model = DealsDetail
        fields = '__all__'

    doctor_name = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Doctor\'s Name'
        })
    )

    product_name = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget = forms.ChoiceWidget(attrs={
            'class': 'custom-select',
        })
    )

    quantity_ordered = forms.CharField(
        widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder':'Enter product quantity',
        })
    )

    employee = forms.CharField(
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'disabled' : 'true'
        })
    )