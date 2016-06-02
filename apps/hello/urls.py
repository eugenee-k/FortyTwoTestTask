from django.conf.urls import patterns
from django.conf.urls import url
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.main, name='main'),
    url(r'^requests/', views.requests, name='requests'),
    url(r'^forajax/', views.forajax, name='forajax'),
    url(r'^forajax_count/', views.forajax_count),

)
