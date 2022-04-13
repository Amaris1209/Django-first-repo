# from django.contrib.auth import get_user_model
# from lib2to3.pgen2 import gari_wala
from django.db import models
import uuid

from gari_wala.models import gari_wala


class insaan(models.Model):
    gari_walaID = models.ForeignKey(gari_wala, on_delete=models.CASCADE, related_name='insaans')
    key = models.UUIDField(primary_key=True ,default=uuid.uuid4, editable=False, unique=True)# this unique key related to Hash
    name = models.CharField(max_length=250, default='')
    gari_walaName= models.CharField(max_length=250, default='')
    email =models.EmailField(default='email')
    pickLat = models.FloatField(default=0)
    pickLong = models.FloatField(default=0)
    dropLat = models.FloatField(default=0)
    dropLong = models.FloatField(default=0)
    # rating = models.FloatField()
    # user = models.ForeignKey(verbose_name=('owner'), to=User,
    #              related_name="my_Feedback",blank = True, on_delete=models.CASCADE)
    city = models.CharField(max_length=250, default='')
    country = models.CharField(max_length=250, default='')
    insaanAddress = models.CharField(max_length=250, default='')
    nic = models.IntegerField(default=0)