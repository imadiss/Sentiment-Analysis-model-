from django.shortcuts import render
from .my_model import prediction
from django.db import connection
import datetime as dt
def index(request):
    res = None
    if request.method == "POST":
        text = request.POST.get('text')
        if text:
            res = prediction(text)
            client_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
            date_time=dt.datetime.now()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO DATA (INPUT, OUTPUT, IP_ADDRESS, DATE_TIME) VALUES (%s, %s, %s, %s)", [text, res, client_ip,date_time])
        else:
            res = "Please enter some text for analysis."
    return render(request, 'index.html', {'result': res})

def about(request):
    return render(request,'about.html')
