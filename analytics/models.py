from django.db import models


class Visitors(models.Model):
    path = models.CharField(max_length=250, blank=True, null=True)
    user_agent = models.CharField(max_length=250, blank=True, null=True)
    ip_add = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
