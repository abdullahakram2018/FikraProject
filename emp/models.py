from django.db import models
from django.contrib.auth.models import User
from group.models import Branch

# Create your models here.
class Jobs(models.Model):
    job = models.CharField(max_length=190,null=True)
    note = models.TextField(null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_jobs_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_jobs_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

class Employees(models.Model):
    name = models.CharField(max_length=190,null=True)
    phone = models.CharField(max_length=190,null=True)
    address = models.CharField(max_length=190,null=True)
    note = models.TextField(null=True)
    job = models.ForeignKey(Jobs,on_delete=models.SET_NULL,null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    manager = models.IntegerField(null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_employees_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_employees_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)