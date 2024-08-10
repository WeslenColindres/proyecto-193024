from django.contrib.models import AbstractUser
from django.db import models

class User(AbstractUser):
    age = models.PositiveIntegerField(_('edad'), default=0, help_text=_('Edad dek usuario'))
    phone_number = models.CharField(_('número de teléfono'), max_length=15, blank=True, help_text=_('Número de teléfono del usuario'))
