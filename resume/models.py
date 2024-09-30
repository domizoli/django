from django.db import models

class cv_user(models.Model):
   name        = models.CharField(max_length=80)
   email       = models.EmailField(max_length=254)

   def __str__(self):
      return f"{self.name}"