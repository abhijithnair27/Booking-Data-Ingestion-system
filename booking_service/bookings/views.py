from .models import Booking
from .serializers import BookingSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# API Which will be helping in posting data
@api_view(['POST'])
def create_booking(request):
    serializer = BookingSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


# API Which will be helping in fetching data
@api_view(['GET'])
def get_bookings(request):
    date = request.GET.get('date', None)
    vendor = request.GET.get('vendor', None)

    bookings = Booking.objects.all()

    if date:
        bookings = bookings.filter(booking_date=date)

    if vendor:
        bookings = bookings.filter(vendor=vendor)
    
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)



# API Which will be helping in fetching data on the basis of ID
@api_view(['GET'])
def get_booking(request, id):
    try:
        booking = Booking.objects.get(id=id)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)


# API Which will be helping in deleteing data on the basis of ID
@api_view(['DELETE'])
def delete_booking(request, id):
    try:
        booking = Booking.objects.get(id=id)
        booking.delete()
        return Response({'message': 'Booking deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)



