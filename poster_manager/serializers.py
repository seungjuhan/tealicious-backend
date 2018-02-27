from rest_framework import serializers
from .models import Poster, Event, Host, Image

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('single_event',)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('single_poster',)

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ('single_host',)

class PosterSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)
    hosts = HostSerializer(many=True, read_only=True)
    image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Poster
        fields = ('id', 'image', 'place', 'time', 'content', 'hosts', 'events')
