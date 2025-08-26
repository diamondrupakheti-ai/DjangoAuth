from django.db import models

class user_data(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=16)
    
    def __str__(self):
        return self.username