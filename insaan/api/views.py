from rest_framework.viewsets import ModelViewSet

from ..models import  insaan
from .serializers import insaanSerializer


class insaanCreateViewSet(ModelViewSet):
    queryset = insaan.objects.all()
    serializer_class = insaanSerializer
    # http_method_names = ['post', 'options']