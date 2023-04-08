from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

# Unregister the provided model admin
admin.site.unregister(User)

#Admin Model Customization

# class EmployeeAdmin(admin.ModelAdmin):
#     pass

class UserAdmin(UserAdmin):
    list_display = ['username','first_name', 'last_name', 'email', 'date_joined', 'is_staff']
    list_display_links = ['username']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','company','image','price','employee']

    

    # def image_resized(self, obj):
    #     return format_html(f'<img src="{obj.image.url}" style="width: 50px; height: 50px">')

# Register your models here.

admin.site.register(User, UserAdmin)
# admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Doctor)
admin.site.register(DoctorSchedule)
admin.site.register(DealsDetail)