from rest_framework import generics
from .serializers import PosterSerializer
from .models import Poster

class PosterList(generics.ListAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

class PosterUpdate(generics.RetrieveDestroyAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer
