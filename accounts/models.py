from ast import Store
from django.db import models
from django.contrib.auth.models import User
from group.models import Branch , TypePro
from sales.models import Product, Unit


# Create your models here.

def customer_photo_directory(instance, filename):
    return 'customers/{0}_{1}'.format(instance.id, instance.name)


    
    
class Account(models.Model):
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    type = models.ForeignKey(TypePro,on_delete=models.SET_NULL,null=True)
    hb = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    lb = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    balance = models.DecimalField(max_digits=6, decimal_places=0)
    trname = models.CharField(max_length=200,null=True)
    photo = models.ImageField(upload_to=customer_photo_directory, null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    username = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='leaves')
    note = models.TextField(null=True)
    adderss = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20, null=True)
    tele = models.CharField(max_length=20, null=True)
    fax = models.CharField(max_length=20, null=True)
    whatsapp = models.CharField(max_length=20, null=True)
    web = models.CharField(max_length=190, null=True)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_account_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_account_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name
    
    

class Currency(models.Model):
    name = models.CharField(max_length=190)
    code = models.CharField(max_length=3,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_currency_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_currency_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
class Balance(models.Model):
    Account = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True,related_name='creditor_order_set')
    currency = models.ForeignKey(Currency,on_delete=models.SET_NULL,null=True)
    balance  = models.DecimalField(max_digits=6, decimal_places=0)

    

class Exchange(models.Model):
    currency = models.ForeignKey(Currency,on_delete=models.SET_NULL,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_exchange_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_exchange_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.price
    
class Order(models.Model):
    #البيان او الملاحضات
    note = models.TextField(null=True)
    #قيمة الفاتورة او الحركة
    total_price = models.FloatField(  default=0 ,null=True)
    #تاريخ الحركة
    date = models.DateField(null=True)
    #  الدائن
    creditor = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True,related_name='creditor_order_set')
    #  المدين
    debitor = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True,related_name='debitor_order_set')
    #رقم المالية او الفاتورة او المستند
    finance = models.CharField(max_length=190,null=True)
    #اعتماد الحركة او تاكيده
    success = models.BooleanField(default=False)
    # نوع الحركة
    type = models.ForeignKey(TypePro,on_delete=models.SET_NULL,null=True)
    # عمولة الحركة
    currency = models.ForeignKey(Currency,on_delete=models.SET_NULL,null=True,related_name='currency_order_set')
    #المرفقات
    attached = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    #الفرع
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_order_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_order_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return 'Order {0}'.format(self.id)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    unit = models.ForeignKey(Unit,on_delete=models.SET_NULL,null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0,null=True)
    stors = models.ForeignKey(Store,on_delete=models.SET_NULL,null=True)
    attached = models.IntegerField(null= True)
    note = models.TextField(null=True)
    success = models.BooleanField(default=False, null=True) 
    attached = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None, null=True)






    
