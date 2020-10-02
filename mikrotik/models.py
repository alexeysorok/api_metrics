from django.db import models

# Create your models here.


class MetricMikrotik(models.Model):
    host = models.CharField(max_length=150)
    traff_uploads = models.IntegerField()
    traff_download = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
