from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=200,
            help_text="Enter Make of Vehicle (i.e. Chevy",
            validators=[MinLengthValidator(limit_value=2, message="Must Enter more than 2 characters")]
            )

    def __str__(self):
        return self.name

class Auto(models.Model):
    nickname = models.CharField(max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")])

    make = models.ForeignKey('Make', on_delete=models.CASCADE)
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)

    def __str__(self):
        return self.nickname
