from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
    name_ar = models.CharField(max_length=190, null=True)
    name_en = models.CharField(max_length=190, null=True)
    logo = models.ImageField(blank=True, null=True)
    

class TypePro(models.Model):
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_typepro_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_typepro_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name

class Project(models.Model):
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    name_ar = models.CharField(max_length=190, null=True)
    name_en = models.CharField(max_length=190, null=True)
    address_ar = models.CharField(max_length=190, null=True)
    address_en = models.CharField(max_length=190, null=True)
    logo = models.ImageField(blank=True, null=True)
    start = models.CharField(max_length=190, null=True)
    typepro = models.ForeignKey(TypePro, null=True, on_delete=models.SET_NULL)
    note_ar = models.TextField(null=True)
    note_en = models.TextField(null=True)
    email = models.CharField(max_length=190, null=True)
    phone = models.CharField(max_length=20, null=True)
    tele = models.CharField(max_length=20, null=True)
    fax = models.CharField(max_length=20, null=True)
    whatsapp = models.CharField(max_length=20, null=True)
    web = models.CharField(max_length=190, null=True)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_project_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_project_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)
    def __str__(self):
        return self.name_ar

        
class Branch(models.Model):
    project = models.ForeignKey(Project,on_delete=models.SET_NULL,null=True)
    place =  models.CharField(max_length=190)
    adderss = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20, null=True)
    tele = models.CharField(max_length=20, null=True)
    fax = models.CharField(max_length=20, null=True)
    whatsapp = models.CharField(max_length=20, null=True)
    web = models.CharField(max_length=190, null=True)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_branch_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_branch_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)
    def __int__(self):
        return self.pk