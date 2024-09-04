from django.db import models


class Pagination(models.Model):
    table_name = models.CharField(max_length=255)
    page_number = models.IntegerField()
    page_size = models.IntegerField()
    total_records = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
