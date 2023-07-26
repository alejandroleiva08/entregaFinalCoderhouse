from django.shortcuts import render

# Create your views here.

#from .models import Cliente

def home(request):
    return render(request, "Cliente/index.html")
