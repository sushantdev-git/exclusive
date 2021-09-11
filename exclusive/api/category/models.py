from django.db import models

# Create your models here.
#here we define our models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        #this function will try to show proper name of category objects rather than generic names.
        return self.name

