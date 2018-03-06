from rest_framework import serializers
from .models import Poster, Event, Host, Image

"""
Used Nested Serializer to serialize "events", "hosts", "image" fields.

TODO:   Convert image into appropriate form of JSON.
        Now, I just send images like "http://127.0.0.1:8000/posters/poster-11-1.JPG"

"""

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('single_event',)

class ImageSerializer(serializers.ModelSerializer):
    single_poster = serializers.ImageField(use_url=True)

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
