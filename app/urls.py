from django.urls import path, include

from app.views import *

app_name = 'app'

urlpatterns = [
    path('wife/',wife,name='wife'),
    path('husband/',husband,name='husband'),
]