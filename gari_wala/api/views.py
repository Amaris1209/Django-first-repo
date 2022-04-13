from rest_framework.viewsets import ModelViewSet

from ..models import gari_wala
from .serializers import gari_walaSerializer


class gari_walaCreateViewSet(ModelViewSet):
    queryset = gari_wala.objects.all()
    serializer_class = gari_walaSerializer
    # http_method_names = ['post', 'options']