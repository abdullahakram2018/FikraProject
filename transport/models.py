from sales.models import Store
from django.db import models
from accounts.models import Currency
from emp.models import Employees
from django.contrib.auth.models import User
from group.models import Branch, TypePro

# Create your models here.

class Cars(models.Model):
    name_car = models.CharField(max_length=190,null=True)
    type_car = models.CharField(max_length=190,null=True)
    model_car = models.CharField(max_length=190,null=True)
    color_car = models.CharField(max_length=190,null=True)
    id_car = models.CharField(max_length=190,null=True)
    date_car = models.CharField(max_length=190,null=True)
    number_car = models.CharField(max_length=190,null=True)
    traffic_code = models.CharField(max_length=190,null=True)
    customs_number = models.CharField(max_length=190,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_cars_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_cars_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
class drivers(models.Model):
    car =  models.ForeignKey(Cars,on_delete=models.SET_NULL,null=True)
    driver =  models.ForeignKey(Employees,on_delete=models.SET_NULL,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_drivers_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_drivers_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)



class Policy(models.Model):
    sender_name = models.CharField(max_length=190,null=True)
    sender_phone =  models.CharField(max_length=190,null=True)
    sender_place =  models.CharField(max_length=190,null=True)
    recipient_name = models.CharField(max_length=190,null=True)
    recipient_phone =  models.CharField(max_length=190,null=True)
    recipient_place =  models.CharField(max_length=190,null=True)
    emp =  models.ForeignKey(Employees,on_delete=models.SET_NULL,null=True)
    date = models.DateField(null=True)
    total_price = models.FloatField(  default=0 ,null=True)
    currency = models.ForeignKey(Currency,on_delete=models.SET_NULL,null=True,related_name='currency_policy_set')
    payment_type = models.ForeignKey(TypePro,on_delete=models.SET_NULL,null=True)
    payment_place =  models.CharField(max_length=190,null=True)
    note = models.TextField(null=True)
    attached_sender = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    attached_recipient = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_policy_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_policy_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
class PolicyItem(models.Model):
    policy = models.ForeignKey(Policy,on_delete=models.SET_NULL,null=True)
    types =  models.CharField(max_length=190,null=True)
    content =  models.CharField(max_length=190,null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True)
    details =  models.CharField(max_length=190,null=True)
    attachment_id =  models.CharField(max_length=190,null=True)
    attachment_date =  models.CharField(max_length=190,null=True)
    note = models.TextField(null=True)

class PolicyStores(models.Model):
    policy = models.ForeignKey(Policy,on_delete=models.SET_NULL,null=True)
    stors = models.ForeignKey(Store,on_delete=models.SET_NULL,null=True)
    emp =  models.ForeignKey(Employees,on_delete=models.SET_NULL,null=True)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_policystore_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_policystore_set')


class PoilcyRelay(models.Model):
    policy = models.ForeignKey(Policy,on_delete=models.SET_NULL,null=True)
    stors = models.ForeignKey(Store,on_delete=models.SET_NULL,null=True)
    car =  models.ForeignKey(Cars,on_delete=models.SET_NULL,null=True)
    driver =  models.ForeignKey(Employees,on_delete=models.SET_NULL,null=True)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_policyrelay_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_policyrelay_set')

    