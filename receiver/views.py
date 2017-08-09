from rest_framework import status, viewsets

from .models import MQTTAction
from .serializers import MQTTActionSerializer


# Create your views here.
class MQTTActionViewSet(viewsets.ModelViewSet):
    queryset = MQTTAction.objects.all()
    serializer_class = MQTTActionSerializer
    http_method_names = ['get', 'post']
