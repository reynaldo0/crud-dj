from django.db import models

class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    country=models.CharField(max_length=30)