from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User


def login_success(sender, request, user, **kwargs):
    print("----------login_success----------")
    print("Login signal")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print(f"kwargs:, {kwargs}")

user_logged_in.connect(login_success,sender=User)


def logout_success(sender, request, user, **kwargs):
    print("----------logout_success----------")
    print("Login signal")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print(f"kwargs:, {kwargs}")
user_logged_out.connect(logout_success,sender=User)

def login_failed(sender, credentials,request, **kwargs):
    print("----------login_failed-signal----------")
    print("Login failed signal")
    print("sender:", sender)
    print("credentials:", credentials)
    print("request:", request)
    print(f"kwargs:, {kwargs}")
user_login_failed.connect(login_failed)