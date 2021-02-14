from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


# Create your models here.
class account(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    modeOfPayment=models.CharField(max_length=250)
    income=models.IntegerField()
    debit=models.IntegerField()
    tellerNo=models.IntegerField()
    dateOfPayment=models.CharField(max_length=20)
    addressOfPayee=models.CharField(max_length=150)
    class Meta:
        db_table='account'
class accountAdmin(admin.ModelAdmin):
    list_display=('name', 'description')

class receipt(models.Model):
    Cusname=models.CharField(max_length=200)
    description=models.TextField()
    date_added=models.DateTimeField()
    amount_paid=models.IntegerField()
    total=models.IntegerField()
    balance=models.IntegerField()
    phone=models.IntegerField()
    class Meta:
        db_table='receipt'
class receiptAdmin(admin.ModelAdmin):
 list_display=('Cusname', 'description')

class teaching(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    midname=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    dob=models.DateTimeField()
    tel=models.IntegerField()
    maritalstatus=models.CharField(max_length=20)
    email=models.EmailField()
    famname=models.CharField(max_length=100)
    villa=models.CharField(max_length=150)
    home=models.CharField(max_length=100)
    lga=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    residence=models.CharField(max_length=250)
    ministry=models.CharField(max_length=50)
    datejoined=models.DateTimeField()
    nextofkin=models.CharField(max_length=150)
    nokadd=models.CharField(max_length=200)
    noktel=models.IntegerField()
    class Meta:
        db_table='teaching'
class teachingAdmin(admin.ModelAdmin):
    list_display=('fname','lname','tel','midname','famname','villa','home','lga','state','nationality','ministry','nextofkin','noktel')

class serviceteam(models.Model):
    name=models.CharField(max_length=200)
    tel=models.IntegerField()
    position=models.CharField(max_length=50)
    date=models.DateTimeField()
    address=models.CharField(max_length=250)
    class Meta:
        db_table='serviceteam'
class serviceteamAdmin(admin.ModelAdmin):
    list_display=('name','position','tel','position','address')
    def __str__(self):
        return self.name

