# from insaan.models import insaan
# from address.api.serializers import AddressSerializer
from insaan.api.serializers import insaanSerializer
from rest_framework import serializers

from ..models import gari_wala


class gari_walaSerializer(serializers.ModelSerializer):
    insaans= insaanSerializer(many=True, read_only=True)
    
    class Meta:
        model = gari_wala
        fields = ['insaans','id','name','email','nic','gari_walaAddress','lat','long','city','country']