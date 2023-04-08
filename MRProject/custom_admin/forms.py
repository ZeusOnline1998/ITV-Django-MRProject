from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from employee.models import DealsDetail, DoctorSchedule


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User

        fields = ['first_name', 'last_name', 'email','username', 'password1', 'password2', 'date_joined', 'is_staff']

    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget = forms.TextInput(attrs={'class': 'form-control','' 'placeholder': 'Employee\'s First Name'})
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget = forms.TextInput(attrs={'class': 'form-control','' 'placeholder': 'Employee\'s Last Name'})
    )

    email = forms.EmailField(
        max_length = 100,
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    username = forms.CharField(
        max_length=100,
        required=True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )

    password1 = forms.CharField(
        min_length=8,
        required=True,
        widget = forms.PasswordInput(attrs= {'class': 'form-control', 'placeholder': 'Enter your password'})
    )

    password2 = forms.CharField(
        min_length=8,
        required=True,
        widget = forms.PasswordInput(attrs= {'class': 'form-control', 'placeholder': 'Confirm password'})
    )

    date_joined = forms.DateField(
        widget = forms.DateInput(attrs={
            'type': 'date'
        })
    )

class AdminProductForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name']


    first_name = forms.ModelChoiceField(
        queryset=User.objects.values_list('first_name', flat=True),
        widget = forms.Select()
    )


class AdminDealsDetailForm(forms.ModelForm):

    class Meta:
        model = DealsDetail
        fields = ['employee']

    employee = forms.ModelChoiceField(
        queryset=User.objects.values_list('first_name', flat=True),
        widget = forms.Select()
    )

class AdminDoctorScheduleForm(forms.ModelForm):

    class Meta:
        model = DoctorSchedule
        fields = ['employee']

    employee = forms.ModelChoiceField(
        queryset=User.objects.values_list('first_name', flat=True),
        widget = forms.Select()
    ) 