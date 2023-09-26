from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    balance = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
