from django.shortcuts import render
from tools.models import Tools

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    tools = Tools.objects.all().order_by('order')
    return render(request, 'core/about.html', {'tools': tools})

def habilities(request):
    return render(request, 'core/habilities.html')