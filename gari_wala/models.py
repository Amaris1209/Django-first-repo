from django.contrib.auth import get_user_model
from django.db import models
import uuid


class gari_wala(models.Model):
    id = models.UUIDField(primary_key=True ,default=uuid.uuid4, editable=False, unique=True)# this unique key related to Hash
    name = models.CharField(max_length=250, default='')
    # rating = models.FloatField()
    # user = models.ForeignKey(verbose_name=('owner'), to=User,
    #              related_name="my_Feedback",blank = True, on_delete=models.CASCADE)
    city = models.CharField(max_length=250, default='')
    country = models.CharField(max_length=250, default='')
    gari_walaAddress = models.CharField(max_length=250, default='')
    nic = models.IntegerField(default=0)
    email =models.EmailField(default='email')
    lat = models.FloatField()
    long = models.FloatField()