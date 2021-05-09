from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Muser(models.Model):
    muser = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    status = models.IntegerField(default = 0)

    def __str__(self):
        return self.muser.username


class Raja(models.Model):
    col_1=models.CharField(max_length=200)
    col_2=models.TextField()
    col_3=models.DateTimeField("date-published")
    col_4=models.CharField(max_length=200)

    def __str__(self):
        return self.col_1


class Contact(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=200)
    message=models.TextField(max_length=400)

    def __str__(self):
        return self.firstname

class RentVehichle(models.Model):
    username= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    fullname= models.CharField(max_length=200)
    dept_name=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    whatsapp_no=models.IntegerField(default=0)
    status=models.IntegerField(default=0)
    
    shop_photo = models.ImageField(upload_to='vehichle images',default='')
    
    def __str__(self):
        return self.fullname