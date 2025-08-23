from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

no_of_guests = models.PositiveIntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(6)]
)


# Create your models here.
class Booking(models.Model):
    id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(11)])
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MaxValueValidator(6)])
    booking_date = models.DateField(default=timezone.now)  
    
    def __str__(self):
        return f"Booking {self.id}: {self.name} for {self.no_of_guests} guests on {self.booking_date}"


class MenuItem(models.Model):
    id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(11)],)
    title =models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(validators=[MaxValueValidator(5)])
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'