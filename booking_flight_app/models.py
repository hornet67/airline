from django.db import models




# Create your models here.


            #  Flight_Schedule models for Admin

class Flight_Schedule(models.Model):
    types = {
        ('Economy','Economy'),
        ('Premime Economy', 'Premime Economy'),
        ('Business', 'Business'),
        ('First','First'),
        ('Multiple','Multiple'),

    }

    days = {
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),

    }


    Flight_name = models.CharField(max_length=100)
    Flight_type = models.CharField(max_length= 20,choices=types)
    Flight_day = models.CharField(max_length=30,choices=days)
    Flight_date =models.DateField(auto_now_add=False,auto_now=False)
    Flight_time = models.TimeField(auto_now_add=False, auto_now=False)
    Destination = models.CharField(max_length=50)

    def __str__(self):
        return self.Flight_name



            #Customer registration models to the website

class Registration(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length = 200,unique=True)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return  self.Name

        # Customer Login models to the website

class Login(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=200, unique=True)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return self.Name





        #Customer Flight booking models


class Booking(models.Model):

    ticket = {
        ('Standard', 'Standard'),
        ('VIP', 'VIP'),
    }

    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length = 200)
    Phone = models.IntegerField()
    Date = models.DateField(auto_now_add=False, auto_now=False)
    Ticket_type = models.CharField(max_length= 50 , choices = ticket)
    Comment = models.TextField(max_length = 300)

    def __str__(self):
        return self.Name





