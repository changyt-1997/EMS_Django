from django.db import models

# Create your models here.


class home(models.Model):
    name = models.CharField(max_length=20)
    salary = models.IntegerField()
    age = models.SmallIntegerField()

    class Meta:
        db_table = 't_home'