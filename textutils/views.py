# I have made this file - Roshan
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("<h1>Home</h1>")

def anal(request):
    djtext = request.GET.get('text', 'default')
    punctuations = '''(/[-[\]{}()*+?.,\\^$|#\s]/g, "\\$&")'''
    analyzed = ""
    for char in djtext:
        if char not in punctuations:
            analyzed += char

    params = {'purpose':'Removed punctuations', 'text':anal_text}
    return render(request, 'anal.html', params)