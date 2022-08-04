from django.shortcuts import render
from .models import Flight_Schedule
#form import
from booking_flight_app.form import RegistrationForm,BookingForm,LoginForm

# Create your views here.

def Schedule(request):
    Flight = Flight_Schedule.objects.all()



    return render(request,'Filght shedule LIst.html',{'title':'shedule','Flight':Flight})


# create registration page views


def Register(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()


    return render(request,'register.html',{'title':'Register Form', 'form':form})

# create login page views

def Login(request):

    form = LoginForm

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()


    return render(request,'Login.html',{'title':'Login Form','form':form})


# create booking page views

def Booking(request):
    form=BookingForm

    if request.method == 'POST':

        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()


    return render(request, 'booking.html', {'title': 'Flight Booking', 'form':form})


def Data_delete(request,F_id):
    Flight = Flight_Schedule.objects.get(pk = F_id).delete()

    return render(request,'delete data.html',{'message':'data Deleted', 'Flight':Flight})

#
