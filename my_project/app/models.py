from django.db import models

# Create your models here

class data(models.Model):
    text = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.text

