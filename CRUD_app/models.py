from django.db import models

# Create your models here.
class Task(models.Model):
    Id =models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Username = models.CharField(max_length=40)
    Email =models.EmailField()

    def __str__(self):
        return self.Name


    

