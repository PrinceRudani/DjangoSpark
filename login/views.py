from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render

from utils.my_logger import get_logger

logger = get_logger()


def admin_load_login(request):
    return render(request, "admin/login&register/login.html")


def generate_token(user_id, username, role):
    access_token_expiry = timedelta(
        seconds=settings.TIME['ACCESS_TOKEN_MAX_AGE'])
    refresh_token_expiry = timedelta(
        seconds=settings.TIME['REFRESH_TOKEN_MAX_AGE'])

    access_token = jwt.encode({
        'user_id': user_id,
        'username': username,
        'role': role,
        'exp': datetime.utcnow() + access_token_expiry
    }, settings.KEYS['JWT_SECRET_KEY'], algorithm='HS256')

    refresh_token = jwt.encode({
        'user_id': user_id,
        'username': username,
        'role': role,
        'exp': datetime.utcnow() + refresh_token_expiry
    }, settings.KEYS['JWT_SECRET_KEY'], algorithm='HS256')

    return access_token, refresh_token


def refresh_token_view(request):
    # Retrieve refresh token from cookies
    refresh_token = request.COOKIES.get(settings.TOKENS['REFRESHTOKEN'])

    if not refresh_token:
        return redirect('/login')  # No refresh token, redirect to login

    try:
        # Decode the refresh token
        data = jwt.decode(refresh_token, settings.KEYS['JWT_SECRET_KEY'],
                          algorithms=['HS256'])
        user_id = data['user_id']
        username = data['username']
        role = data['role']

        # Generate new access and refresh tokens
        access_token, new_refresh_token = generate_token(user_id, username,
                                                         role)

        # Set new tokens in cookies
        response = redirect(
            '/home')  # Redirect to the protected home view or dashboard
        response.set_cookie(settings.TOKENS['ACCESSTOKEN'], access_token,
                            max_age=settings.TIME['ACCESS_TOKEN_MAX_AGE'],
                            httponly=True)
        response.set_cookie(settings.TOKENS['REFRESHTOKEN'], new_refresh_token,
                            max_age=settings.TIME['REFRESH_TOKEN_MAX_AGE'],
                            httponly=True)

        return response

    except jwt.ExpiredSignatureError:
        # Handle expired token
        return redirect('/login?error=refresh_token_expired')

    except jwt.InvalidTokenError:
        # Handle invalid token
        return redirect('/login?error=invalid_token')


def login_required(fn):
    def wrapped_view(request, *args, **kwargs):
        access_token = request.COOKIES.get(settings.TOKENS['ACCESSTOKEN'])

        if not access_token:
            return redirect(
                '/')  # Redirect to login if access token is missing

        try:
            # Decode the access token
            data = jwt.decode(access_token, settings.KEYS['JWT_SECRET_KEY'],
                              algorithms=['HS256'])
            request.user = data  # You can set the user in the request object if needed
            return fn(request, *args, **kwargs)

        except jwt.ExpiredSignatureError:
            # If the token is expired, redirect to the refresh token view
            return redirect('/refresh-token')

        except jwt.InvalidTokenError:
            # If the token is invalid, redirect to login
            return redirect('/login?error=invalid_token')

    return wrapped_view


def add_to_blacklist(token):
    """Add a token to the blacklist."""
    jti = jwt.get_unverified_header(token)['jti']
    cache_key = f"blacklisted_token_{jti}"
    cache.set(cache_key, token, settings.TIME['ACCESS_TOKEN_MAX_AGE'])

def is_blacklisted(token):
    """Check if a token is blacklisted."""
    jti = jwt.get_unverified_header(token)['jti']
    cache_key = f"blacklisted_token_{jti}"
    return cache.get(cache_key) is not None