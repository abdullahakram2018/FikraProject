from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    success = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )