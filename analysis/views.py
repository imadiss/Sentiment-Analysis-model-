from django.shortcuts import render
from .my_model import prediction

def index(request):
    res=None
    if request.method == "POST":
        text=request.POST.get('text')
        if text:
            res=prediction(text)
        else:
            res = "Please enter some text for analysis."
    return render(request,'index.html',{'result':res})

def about(request):
    return render(request,'about.html')
