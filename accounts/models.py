# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class CustomUser(AbstractUser):
    address = models.CharField(max_length=150, null=True, blank=True)
    login_cnt = models.IntegerField(default=0) # increments
    restriction_date = models.DateTimeField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self.is_active = False
    #     # if not self.is_superuser:
    #     #     # self.is_superuser = False
    #     #     self.is_active = False
