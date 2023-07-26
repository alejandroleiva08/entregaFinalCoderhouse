from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#from .models import Cliente

# Create your views here.
def home(request):
    return render(request, "CORE/index.html")
