from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Measures, UserAttributes
from .serializers import MeasuresSerializer, UserAttributesSerializer

class MeasuresViewSet(viewsets.ModelViewSet):
    queryset = Measures.objects.all()
    serializer_class = MeasuresSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Measures.objects.filter(user=self.request.user)


class UserAttributesListCreateView(generics.ListCreateAPIView):
    queryset = UserAttributes.objects.all()
    serializer_class = UserAttributesSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserAttributes.objects.filter(user=self.request.user)
