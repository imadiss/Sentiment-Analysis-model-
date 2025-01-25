from django.db import models

class Data(models.Model):
    input_text = models.TextField()
    output_text = models.CharField(max_length=10)
