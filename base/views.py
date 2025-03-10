from django.shortcuts import render
from utils.my_logger import get_logger

logger = get_logger()
def home(request):
    logger.info(' load Home Page ')
    return render(request, 'admin/home.html')

