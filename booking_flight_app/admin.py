from django.contrib import admin
from .models import Flight_Schedule,Registration,Booking,Login

# Register your models here.

class Flight_Schedule_ad(admin.ModelAdmin):
    list_display = ['Flight_name', 'Flight_type', 'Flight_day', 'Flight_date','Destination']
    list_filter = ['Flight_type', 'Flight_day',]


admin.site.register(Flight_Schedule,Flight_Schedule_ad)
admin.site.register(Registration)
admin.site.register(Booking)
admin.site.register(Login)


