from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('<int:pk>', views.PosterUpdate.as_view()),
    path('', views.PosterList.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
