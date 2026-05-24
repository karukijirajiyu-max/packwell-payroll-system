from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SalaryRecord
from employees.models import Employee

@login_required
def dashboard(request):

    employee = Employee.objects.get(
        user=request.user
    )

    salary_records = SalaryRecord.objects.filter(
        employee=employee
    ).order_by('-month')

    return render(
        request,
        'dashboard.html',
        {
            'salary_records': salary_records
        }
    )