from django.http import HttpResponse
from django.shortcuts import render
#routes
def home(request):
    return render(request,'website/index.html')
    # return HttpResponse('hello world:home')

def about(request):
    return render(request,'website/about.html')
    # return HttpResponse('hello world:about')

def contact(request):
    return render(request,'website/contact.html')
    return HttpResponse('hello world:contact')