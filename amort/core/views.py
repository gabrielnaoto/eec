from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {'msg': 'oi mundo, td bem?'})