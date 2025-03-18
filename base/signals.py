from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)
from django.dispatch import receiver
from django.utils.timezone import now
import logging

logger = logging.getLogger(__name__)


# Helper function to get client details
def get_client_info(request):
    """Helper function to get client IP, user agent details, and server name"""
    ip = request.META.get("REMOTE_ADDR", "Unknown IP")
    user_agent = request.META.get("HTTP_USER_AGENT", "Unknown User Agent")
    server_name = request.get_host() if request else "Unknown Server"
    return ip, user_agent, server_name


# Helper function to log messages
def log_message(event_type, user, request, extra_details=""):
    """Helper function to log detailed login/logout events"""
    ip, user_agent, server_name = get_client_info(request)
    timestamp = now()

    log_message = (
        f"Event: {event_type}\n"
        f"Sender: {user.__class__.__name__ if user else 'Unknown Sender'}\n"
        f"Receiver: {event_type.lower()}\n"
        f"Server: {server_name}\n"
        f"User: {user.username if user else 'Unknown User'} (ID: {user.id if user else 'Unknown ID'})\n"
        f"Email: {user.email if user else 'Unknown Email'}\n"
        f"IP: {ip}\n"
        f"Browser: {user_agent}\n"
        f"Timestamp: {timestamp}\n"
        f"{extra_details}"
        "--------------------------------------"
    )

    # Print and log the message
    print(log_message)
    logger.info(log_message)


# Signal for login success
@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    """Log successful login events"""
    log_message("LOGIN SUCCESS", user, request)


# Signal for logout event
@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    """Log logout events"""
    log_message("LOGOUT EVENT", user, request)


# Signal for login failure
@receiver(user_login_failed)
def log_login_failed(sender, credentials, request, **kwargs):
    """Log failed login attempts"""
    ip, user_agent, server_name = get_client_info(request)
    username = credentials.get("username", "Unknown Username")

    # Log failed login attempt
    log_message(
        "LOGIN FAILED", None, request, extra_details=f"Attempted Username: {username}\n"
    )
    logger.warning(
        f"Login failed for username: {username} from IP: {ip}, Browser: {user_agent}"
    )
