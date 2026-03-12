from django.db import models

class Property(models.Model):

    title = models.CharField(max_length=200)
    price = models.IntegerField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title