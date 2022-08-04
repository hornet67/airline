from django import forms
from pyexpat import model

from .models import Registration,Booking,Login


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = '__all__'

