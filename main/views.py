from django.shortcuts import render
import logging


logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    logger.info('User has accessed the index page')
    return render(request, 'main/home.html')