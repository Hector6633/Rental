from django.db import models

# Create your models here.
class Premium_Car_Model(models.Model):
    car_img = models.ImageField(upload_to='media')
    car_name = models.CharField(max_length=25)
    rent_price = models.CharField(max_length=6)
    # specification
    seat = models.IntegerField()
    fuel = models.CharField(max_length=8)
    model = models.IntegerField()
    transmission = models.CharField(max_length=6)
    
    def __str__(self) -> str:
        return self.car_name

class Car_Reservation(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    purpose = models.CharField(max_length=20)
    car_model = models.CharField(max_length=25)
    pickup_location = models.CharField(max_length=20)
    dropoff_location = models.CharField(max_length=20)
    pickup_date = models.CharField(max_length=10)
    pickup_time = models.CharField(max_length=8)
    dropoff_date = models.CharField(max_length=10)
    dropoff_time = models.CharField(max_length=8)
    
    def __str__(self) -> str:
        return self.name
    
class Premium_Car_Reservation(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    purpose = models.CharField(max_length=20)
    car_model = models.CharField(max_length=25)
    pickup_location = models.CharField(max_length=20)
    dropoff_location = models.CharField(max_length=20)
    pickup_date = models.CharField(max_length=10)
    pickup_time = models.CharField(max_length=8)
    dropoff_date = models.CharField(max_length=10)
    dropoff_time = models.CharField(max_length=8)
    
    def __str__(self) -> str:
        return self.name
    

    