from django.db import models

# Create your models here.


class Workshift(models.Model):
    start_date = models.DateTimeField
    end_date = models.DateTimeField
    car_number = models.PositiveSmallIntegerField
    brake_times = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.car_number