from rest_framework import viewsets
from .models import Measures
from .serializers import MeasuresSerializer

class MeasuresViewSet(viewsets.ModelViewSet):
    queryset = Measures.objects.all()
    serializer_class = MeasuresSerializer