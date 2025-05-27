from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):  # username, password, email, firstname, lastname already satisfied
    date_of_birth = models.DateField(verbose_name="تاریخ تولد", blank=True, null=True)
    bio = models.TextField(verbose_name="بایو", null=True, blank=True)
    photo = models.ImageField(verbose_name="تصویر", upload_to="profile_images/", null=True, blank=True)
    job = models.CharField(verbose_name="شغل", max_length=25, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="شماره تماس")
