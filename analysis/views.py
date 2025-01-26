from django.shortcuts import render
from .my_model import prediction
from django.db import connection

def index(request):
    res = None
    if request.method == "POST":
        text = request.POST.get('text')
        if text:
            res = prediction(text)
            client_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO DATA (INPUT, OUTPUT, IP_ADDRESS) VALUES (%s, %s, %s)", [text, res, client_ip])
        else:
            res = "Please enter some text for analysis."
    return render(request, 'index.html', {'result': res})

def about(request):
    return render(request,'about.html')
