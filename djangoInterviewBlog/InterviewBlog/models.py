from django.db import models


# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=200, null=True)
    program_of_study = models.CharField(max_length=200, null=True)
    graduation_year = models.CharField(max_length=4, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

