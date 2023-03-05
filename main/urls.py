from django.urls import path
from .views import *

urlpatterns = [
    path('', get_price, name='get_price'),

]