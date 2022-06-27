# i have created this file - Akash
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    print(djtext)
    removepunc = request.POST.get('removepunc', 'off')
    FullCaps = request.POST.get('FullCaps', 'off')
    Newlineremover = request.POST.get('Newlineremover', 'off')
    ExtraSpaceRemover = request.POST.get('ExtraSpaceRemover', 'off')
    CharCounter = request.POST.get('CharCounter', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if FullCaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed

    if Newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if ExtraSpaceRemover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if CharCounter == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = len(djtext)
        params = {'purpose': 'characters counter', 'analyzed_text': analyzed}
        djtext = analyzed

    if removepunc != "on" and FullCaps != "on" and Newlineremover != "on" and ExtraSpaceRemover != "on" and CharCounter != 'on':
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
