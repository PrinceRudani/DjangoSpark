from django.contrib.auth.hashers import make_password, check_password
from django.db import models


# Assuming you have the LoginVO model in your login&register app.

class LoginVO(models.Model):
    login_id = models.AutoField(primary_key=True)
    login_username = models.CharField(max_length=120, unique=True)  # Ensure unique usernames
    login_password = models.CharField(max_length=120)  # Consider using hashed passwords
    login_role = models.CharField(max_length=120)

    LOGIN_STATUS_CHOICES = [(0, 'Inactive'), (1, 'Active'),]
    login_status = models.IntegerField(choices=LOGIN_STATUS_CHOICES, default=0)  # Use choices for clarity

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.login_username

    class Meta:
        db_table = 'login_table'
        verbose_name = 'Login'
        verbose_name_plural = 'Logins'

    def set_password(self, password):
        self.login_password = make_password(password)

    # Method to check if password is valid
    def check_password(self, password):
        return check_password(password, self.login_password)
