from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/index.html')

def dashboard2(request):
    return render(request, 'dashboard/base_dashboard.html')