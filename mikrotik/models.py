from django.db import models
from django.utils import timezone
from hurry.filesize import size, si, alternative, verbose, traditional
# Create your models here.


class MetricMikrotik(models.Model):
    host = models.CharField(max_length=150)
    traff_uploads = models.IntegerField()
    traff_download = models.IntegerField()
   # date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Host Name: " + self.host + ", " \
               + "Date: " + str(self.date.astimezone().strftime("%b %d %Y %H:%M:%S")) \
               + ", DOWN: " + size(self.traff_download, system=si) \
               + ", UP: " + size(self.traff_uploads, system=si)

