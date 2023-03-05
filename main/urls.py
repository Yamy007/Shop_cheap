from django.urls import path
from .views import *

urlpatterns = [
    path('', silpo, name='get_price'),

]