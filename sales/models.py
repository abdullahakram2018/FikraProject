from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account, Currency
from group.models import Branch, TypePro

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=190)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_company_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_company_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
class Store(models.Model):
    name = models.CharField(max_length=190,null=True)
    place = models.CharField(max_length=190,null=True)
    tele = models.CharField(max_length=190,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_store_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_store_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name    
    
class Unit(models.Model):
    group = models.CharField(max_length=190)
    name = models.CharField(max_length=190)
    type = models.ForeignKey(TypePro, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_unit_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_unit_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=190)
    group = models.CharField(max_length=190)
    type = models.ForeignKey(TypePro, null=True, on_delete=models.SET_NULL)
    company_item = models.ForeignKey(Company,on_delete=models.SET_NULL,null=True)
    unit = models.ForeignKey(Unit,on_delete=models.SET_NULL,null=True)
    balance = models.DecimalField(max_digits=6, decimal_places=0)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    package = models.FloatField(null=True)
    la = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    ha = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    puprice = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    sprice = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_produt_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_product_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    castomer =  models.ForeignKey(Account,on_delete=models.SET_NULL,null=True,related_name='creditor_invoice_set')
    type = models.ForeignKey(TypePro, null=True, on_delete=models.SET_NULL)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True)
    currency = models.ForeignKey(Currency,on_delete=models.SET_NULL,null=True,related_name='currency_invoice_set')
    success = models.BooleanField(default=False)
    note = models.TextField(null=True)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_invoice_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_invoice_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    unit = models.ForeignKey(Unit,on_delete=models.SET_NULL,null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0,null=True)
    stors = models.ForeignKey(Store,on_delete=models.SET_NULL,null=True)
    note = models.TextField(null=True)
    success = models.BooleanField(default=False, null=True) 


    

    
