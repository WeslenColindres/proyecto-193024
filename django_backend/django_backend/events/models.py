from django.db import models
from businesses.models import Business


class Event(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
