from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)

    class Meta:
        db_table = 't_user'