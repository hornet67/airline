from django.urls import path
from . import views

urlpatterns = [
    path('schedule/',views.Schedule,name='schedule'),
    path('',views.Register, name='register'),
    path('login/',views.Login,name='login'),
    path('booking/',views.Booking, name='booking'),
    path('delete/<int:F_id>',views.Data_delete, name='delete'),

]
