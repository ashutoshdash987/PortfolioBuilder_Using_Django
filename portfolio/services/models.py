from django.db import models

class user(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50,null=True)
    mail = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=14)

