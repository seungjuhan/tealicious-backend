from rest_framework import serializers
from . import Poster

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ('id', 'image', 'place', 'time', 'content', 'hosts', 'events')
