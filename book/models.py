from django.db import models

# Create your models here.
## Define a Book Class
class Book(models.Model):
    ## Name of the book with defined number of characters
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=30,default='anonymous')
    email = models.EmailField(blank=True)
    description = models.TextField(default="No description available")

    def __str__(self):
        return self.name
