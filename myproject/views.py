from django.http import HttpResponse
from django.shortcuts import render
def analyse(request):
    text1=request.POST.get("text")
    removepunc = request.POST.get('removepunc', 'off')
    upper= request.POST.get('upper', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    lengthoftext = request.POST.get('lengthoftext', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text1:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        text1 = analyzed
    if upper=="on":
       analyzed=""
       for char in text1:
           analyzed=analyzed+char.upper()
       params = {'purpose': 'upper case', 'analyzed_text': analyzed}
       text1=analyzed
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(text1):
            if not (text1[index] == " " and text1[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        text1 = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in text1:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        text1= analyzed
    if (lengthoftext=="on"):
        analyzed=len(text1)
        params = {'purpose': 'Length of String', 'analyzed_text': analyzed}
    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and upper != "on" and lengthoftext!="on"):
        return HttpResponse("please select any operation and try again")
    return render(request, 'analyse.html', params)
def index(request):
    return render(request,'index.html')