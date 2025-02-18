from django.db import models

# Create your models here.
class Booking(models.Model):
    customer_name = models.CharField(max_length=255)
    booking_date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    vendor = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.customer_name} - {self.vendor}"


