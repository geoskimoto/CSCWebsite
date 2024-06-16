from django.shortcuts import render
from book.models import Bunk, Room
# Create your views here.

def index(request):
    return render(request, 'book/index.html')
def bunk(request):
    return render(request, 'book/bunk.html')