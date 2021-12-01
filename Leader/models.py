from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=50)
    phno = models.CharField(max_length=14)
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    empid = models.CharField(max_length=20)
    psw = models.CharField(max_length=20)
    cpsw = models.CharField(max_length=20)


# class worklog(models.Model):
#     empid = models.CharField(max_length=20)
#     date = models.DateField()
#     hour1 = models.CharField(max_length=200)
#     remark1 = models.CharField(max_length=200)
#     hour2 = models.CharField(max_length=200)
#     remark2 = models.CharField(max_length=200)
#     hour3 = models.CharField(max_length=200)
#     remark3 = models.CharField(max_length=200)
#     hour4 = models.CharField(max_length=200)
#     remark4 = models.CharField(max_length=200)
#     hour5 = models.CharField(max_length=200)
#     remark5 = models.CharField(max_length=200)
#     hour6 = models.CharField(max_length=200)
#     remark6 = models.CharField(max_length=200)
#     hour7 = models.CharField(max_length=200)
#     remark7 = models.CharField(max_length=200)
#     hour8 = models.CharField(max_length=200)
#     remark8 = models.CharField(max_length=200)


class dailywork(models.Model):
    user=models.CharField(max_length=25,null=True)
    currentdate = models.DateField()
    hour1 = models.CharField(max_length=200)
    hour2 = models.CharField(max_length=200)
    hour3 = models.CharField(max_length=200)
    hour4 = models.CharField(max_length=200)
    hour5 = models.CharField(max_length=200)
    hour6 = models.CharField(max_length=200)
    hour7 = models.CharField(max_length=200)
    hour8 = models.CharField(max_length=200)
    r1 = models.CharField(max_length=200)
    r2 = models.CharField(max_length=200)
    r3 = models.CharField(max_length=200)
    r4 = models.CharField(max_length=200)
    r5 = models.CharField(max_length=200)
    r6 = models.CharField(max_length=200)
    r7 = models.CharField(max_length=200)
    r8 = models.CharField(max_length=200)
    


class suser(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)


class emailus(models.Model):
    contactname = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=200)


