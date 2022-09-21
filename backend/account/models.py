from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomizeUser(AbstractUser):
    email = models.EmailField(_('Email Address'), unique=True)