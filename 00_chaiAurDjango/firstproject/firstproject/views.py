from django.http import HttpResponse
#routes
def home(request):
    return HttpResponse('hello world:home')

def about(request):
    return HttpResponse('hello world:about')

def contact(request):
    return HttpResponse('hello world:contact')