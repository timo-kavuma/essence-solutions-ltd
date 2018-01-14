from django.shortcuts import render
from .models import Content

# Create your views here.
def index(request):
    return render(request, 'Page/home.html')

def detail_1(request, page):
    data = Content.objects.get(pk=page)
    context = {'info': data}
    return render(request, 'Page/detail01.html', context)

def detail_2(request, page):
    data = Content.objects.get(pk=page)
    context = {'info': data}
    return render(request, 'Page/detail02.html', context)

