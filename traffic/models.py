from django.db import models

class TrafficData(models.Model):
    timestamp = models.DateTimeField(editable=True)
    source_ip = models.CharField(max_length=15)
    dest_ip = models.CharField(max_length=15)
    protocol = models.CharField(max_length=10)
    length = models.IntegerField()
    info = models.TextField()
