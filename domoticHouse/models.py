from django.db import models

# Create your models here.


class Room(models.Model):
    room_name = models.CharField(max_length=60, help_text="Enter a room name")
    temperature = models.OneToOneField("TemperatureControl",on_delete=models.SET_NULL, null=True)
    automated_windows = models.OneToOneField("AutomatedWindows",on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.room_name
    
class TemperatureControl(models.Model):
    temperature = models.DecimalField(max_digits=15, decimal_places=4,default="")
    humidity = models.DecimalField(max_digits=15, decimal_places=4,default="")
    
    def __str__(self):
        return str(self.temperature)
    
class AutomatedWindows(models.Model):
    
    number_of_windows = models.IntegerField(default=0)
    hour_programmed = models.TimeField(auto_now=False)
    
    TYPE_WINDOWS = (
        ("p", "Programable"),
        ("f", "fixed"),
    )
    
    type_of_windows = models.CharField(
        max_length=1,
        choices=TYPE_WINDOWS,
        default='f',
        help_text='Type of Automated Window',
    )
    
    
    
    