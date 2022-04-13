# from address.api.serializers import AddressSerializer
# from address.api.serializers import AddressSerializer
from rest_framework import serializers

from ..models import insaan


class insaanSerializer(serializers.ModelSerializer):

    class Meta:
        model = insaan
        fields = ('key','email','gari_walaName','gari_walaID','pickLat','pickLong','dropLat','dropLong', 'insaanAddress','city','country','nic')