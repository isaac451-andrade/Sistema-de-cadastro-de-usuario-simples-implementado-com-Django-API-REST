from django.db import models

class User(models.Model):
    user_nickname = models.CharField(max_length=100, primary_key=True, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"User_name: {self.user_nickname} | User_email: {self.user_email}"
