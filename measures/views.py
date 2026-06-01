from rest_framework import viewsets
from rest_framework import generics
from .models import Measures, UserAttributes
from .serializers import MeasuresSerializer, UserAttributesSerializer

class MeasuresViewSet(viewsets.ModelViewSet):
    queryset = Measures.objects.all()
    serializer_class = MeasuresSerializer

    def get_queryset(self):
        return Measures.objects.filter(user=self.request.user)


class UserAttributesListCreateView(generics.ListCreateAPIView):
    queryset = UserAttributes.objects.all()
    serializer_class = UserAttributesSerializer

    def get_queryset(self):
        return UserAttributes.objects.filter(user=self.request.user)
