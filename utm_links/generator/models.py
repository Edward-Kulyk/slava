from django.db import models

# Create your models here.
from django.db import models
from django.db.models import CharField


class UtmLink(models.Model):
    utm_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    medium = models.CharField(max_length=255)
    campaign = models.CharField(max_length=255)
    content = models.CharField(max_length=255, blank=True, null=True)
    term = models.CharField(max_length=255, blank=True, null=True)
    short_id = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url}"


class ShortIO(models.Model):
    id = models.AutoField(primary_key=True)
    short_link = models.CharField(max_length=255, unique=True)
    parent_link_id = models.IntegerField(blank=True, null=True)
    utm_link = models.ForeignKey(UtmLink, on_delete=models.CASCADE)
    domain = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    link_id = models.CharField(max_length=255)

    def __str__(self):
        return self.short_link

