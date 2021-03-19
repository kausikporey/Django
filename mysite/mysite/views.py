from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def setlink(request):
    return HttpResponse("<h1>Hello World.</h1><STYLE>a:link{text-decoration:none;}</STYLE> <a href='https://youtube.com'>ClickHere</a>") 

def analyzetext(request):
    text = request.POST.get('text','default')
    punc = request.POST.get('removepunc','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('removespace','off')
    capital = request.POST.get('capitalize','off')

    rtext = ""
    if(punc == 'on'):
        punctuations = '''*%;:''"".$,#@!`~&^<>?'''
        for char in text:
            if char not in punctuations:
                rtext = rtext+char
        params = {'purpose':'Remove Punctuations','text':rtext}        
    elif(spaceremove == 'on'):
        for index,char in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                rtext = rtext+char
        params = {'purpose':'Space Remove','text':rtext}          
    elif(newlineremove == 'on'):
        for char in text:
            if char != '\n' and char != '\r':
                rtext = rtext+char
        params = {'purpose':'New Line Remover','text':rtext}          
    elif(capital == 'on'):
        rtext = text.upper()
        params = {'purpose':'Text Capitalize','text':rtext}                           
    else:
        return HttpResponse("Does not Exists..") 

    return render(request,'analyze.html',params)                          