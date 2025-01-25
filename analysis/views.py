from django.shortcuts import render
from .my_model import prediction
from django.db import connection

def index(request):
    res = None
    if request.method == "POST":
        text = request.POST.get('text')
        if text:
            res = prediction(text)

            # Insert the input and result into the database using raw SQL
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO DATA (INPUT, OUTPUT) VALUES (%s, %s)", [text, res])
        else:
            res = "Please enter some text for analysis."
    return render(request, 'index.html', {'result': res})

def about(request):
    return render(request,'about.html')
