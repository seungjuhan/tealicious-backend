from django.contrib import admin

from .models import Poster, Host, Content, Image

admin.site.register(Poster)
admin.site.register(Host)
admin.site.register(Image)
admin.site.register(Content)
