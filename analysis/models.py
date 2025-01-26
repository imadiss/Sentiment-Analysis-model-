from django.db import models

class Data(models.Model):
    id = models.AutoField(primary_key=True)
    input = models.TextField()
    output = models.CharField(max_length=10)
    ip_address = models.CharField(max_length=50)
    date_time = models.DateTimeField()
