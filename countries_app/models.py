from django.db import models

# Create your models here.


class Countries(models.Model):
    # Model inherits from models
    # and Countries inherits from Model
    name = models.CharField(max_length = 50, default='')
    capital = models.CharField(max_length=50, default='')

    # django bydefault makes an id column also

    # to display the name as the object
    def __str__(self):
        return self.name

    class Meta:
        # Meta is the inner class which adds us in ordering the data when an query is made
        ordering=('id', )