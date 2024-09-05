from django.shortcuts import render
from django.http import JsonResponse
from .models import Department

def department_list(request):
    ministry_id = request.GET.get('ministry_id')
    departments = Department.objects.filter(ministry_id=ministry_id)
    options = ['<option value="">---------</option>']  # Default empty option
    for department in departments:
        options.append(f'<option value="{department.id}">{department.name}</option>')
    return JsonResponse(''.join(options), safe=False)