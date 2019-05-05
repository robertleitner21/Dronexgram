from django.db import models

# Create your models here.


from django.db import models

class User(models.Model):
    username = models.CharField(max_length=35)
    email = models.CharField(max_length=68)
    password = models.CharField(max_length=18)
    last_login = models.DateTimeField(auto_now=True)
