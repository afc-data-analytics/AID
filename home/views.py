from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def dashboard(request):
    return render(request, "home/dashboard.html")