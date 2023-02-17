from django.urls import path
from .views import MainPage, LoadFile


urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('load/', LoadFile.as_view(), name='load_file'),
]
