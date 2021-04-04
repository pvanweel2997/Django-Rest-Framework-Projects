# Create your models here.
from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    ratings = models.DecimalField(max_digits=10,decimal_places=3)

    def __str__(self):
        return self.id+self.name+self.description+self.ratings
