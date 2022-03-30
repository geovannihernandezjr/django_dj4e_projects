from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=300,
            help_text="Enter breed of cat (i.e. Sphynx)",
            validators=[MinLengthValidator(2, "Breed name should be 2 or more characters")]
            )

    def __str__(self):
        return self.name

class Cat(models.Model):
    nickname = models.CharField(max_length=300,
            validators=[MinLengthValidator(2, "Nickname should be 2 or more characters")]
            )
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=300)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nickname
