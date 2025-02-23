
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_form'),
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete')
]
