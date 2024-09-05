from typing import Any
from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.db.models.query import QuerySet
from django.http import HttpRequest
from incidents.models import *

# Register your models here.

class AgencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'uid', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'uid')
    search_fields = ('code', 'name')
    ordering = ('name',)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Agency.admin_objects.all()
        else:
            return Agency.objects.all()

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'uid', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'uid')
    search_fields = ('code', 'name')
    ordering = ('name',)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Category.admin_objects.all()
        else:
            return Category.objects.all()

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'code', 'name', 'uid', 'status', 'created_at', 'updated_at')
    list_filter = ('category', 'status', 'uid')
    search_fields = ('category__name', 'code', 'name')
    ordering = ('name',)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Subcategory.admin_objects.all()
        else:
            return Subcategory.objects.all()

class MinistryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'uid', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'uid')
    search_fields = ('code', 'name')
    ordering = ('name',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('ministry', 'code', 'name', 'uid', 'status', 'created_at', 'updated_at')
    list_filter = ('ministry', 'status', 'uid')
    search_fields = ('ministry__name', 'code', 'name')
    ordering = ('name', 'ministry__name')

# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('ministry', 'department', 'code', 'name', 'uid', 'status', 'created_at', 'updated_at')
#     list_filter = ('ministry', 'department', 'status', 'uid')
#     search_fields = ('ministry__name', 'department__name', 'code', 'name')
#     ordering = ('name', 'ministry__name')

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'created_at': AdminDateWidget(),
            'updated_at': AdminDateWidget(),
        }

class LocationAdmin(admin.ModelAdmin):
    form = LocationForm
    list_display = ('ministry', 'department', 'code', 'name', 'uid', 'status', 'created_at', 'updated_at')
    list_filter = ('ministry', 'department', 'status', 'uid')
    search_fields = ('ministry__name', 'department__name', 'code', 'name')
    ordering = ('name', 'ministry__name')

    class Media:
        js = ('admin/js/vendor/jquery/jquery.js', 'admin/js/core.js', 'myapp/js/admin.js')  # Path to your custom JS file

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            form.base_fields['department'].queryset = Department.objects.filter(ministry=obj.ministry)
        return form

class StateAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'uid', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'uid')
    search_fields = ('code', 'name')
    ordering = ('name',)

class StateDepartmentAdmin(admin.ModelAdmin):
    list_display = ('state', 'code', 'name', 'uid', 'status', 'created_at', 'updated_at')
    list_filter = ('state', 'status', 'uid')
    search_fields = ('state__name', 'code', 'name')
    ordering = ('name', 'state__name')

class StateLocationAdmin(admin.ModelAdmin):
    list_display = ('state', 'department', 'code', 'name', 'uid', 'status', 'created_at', 'updated_at')
    list_filter = ('state', 'department', 'status', 'uid')
    search_fields = ('state__name', 'department__name', 'code', 'name')
    ordering = ('name', 'state__name')

admin.site.register(Agency, AgencyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Ministry, MinistryAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(StateDepartment, StateDepartmentAdmin)
admin.site.register(StateLocation, StateLocationAdmin)
