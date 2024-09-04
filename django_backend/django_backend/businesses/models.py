from django.db import models
from users.models import User


class Business(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)


class BusinessCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)


class BusinessCategoryAssignment(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    category = models.ForeignKey(BusinessCategory, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('business', 'category')


class Industry(models.Model):
    name = models.CharField(max_length=255, unique=True)


class BusinessIndustry(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('business', 'industry')


class BusinessImage(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    image = models.BinaryField()
    description = models.TextField(blank=True, null=True)
