from django.urls import path
from .views import create_booking, get_bookings, get_booking, delete_booking


#All urls related to Bookings.
urlpatterns = [
    path('bookings', create_booking, name='create_booking'),
    path('bookings/', get_bookings, name='get_bookings'),
    path('bookings/<int:id>', get_booking, name='get_booking'),
    path('bookings/<int:id>/delete', delete_booking, name='delete_booking'),

]