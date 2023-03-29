from django.db import models
from django.contrib.auth.models import User


class User(User):
    email = models.CharField(max_length=30)
