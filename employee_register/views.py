from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        context = {'form': form, 'employee_form': Employee.objects.all()}
        return render(request, "employee_register/employee_form.html", context)
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
            return redirect('employee_form')
        else: 
            context = {'form': form, 'employee_form': Employee.objects.all()}
            return render (request, 'employee_register/employee_form.html', context,)    


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_form')
