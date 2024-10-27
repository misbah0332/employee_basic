from django.db import models

class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)