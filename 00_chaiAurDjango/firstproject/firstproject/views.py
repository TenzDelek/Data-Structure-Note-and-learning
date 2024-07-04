from django.http import HttpResponse
from django.shortcuts import render
#routes
def home(request):
    return render(request,'website/index.html')
    # return HttpResponse('hello world:home')

def about(request):
    return HttpResponse('hello world:about')

def contact(request):
    return HttpResponse('hello world:contact')