from django.urls import path
from .views import MainPage, LoadFile, EmailHandler


urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('load/', LoadFile.as_view(), name='load_file'),
    path('email_hand/', EmailHandler.as_view(), name='email_handler')
]
