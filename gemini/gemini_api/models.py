from django.db import models


class Report(models.Model):
    image=models.FileField()
    report_text=models.TextField(null=True)
# Create your models here.
