from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render

from login.models import LoginVO
from login.views import generate_token, login_required


@login_required
def home(request):
    return render(request, "admin/home.html")


def load_home_page(request):
    if request.method == "POST":
        try:
            # Collect data for login attempt
            username = request.POST.get("register_username", "").strip()
            password = request.POST.get("register_password", "").strip()

            if not username or not password:
                raise ValueError("Username and password are required.")

            # Validate user credentials
            user = LoginVO.objects.get(login_username=username)
            if not user.check_password(password):
                raise ValueError("Invalid password.")

            # Validate user role
            if user.login_role not in [settings.ROLES["ADMIN"], settings.ROLES["USER"]]:
                raise ValueError("Invalid user role.")

            # Generate new tokens
            access_token, refresh_token = generate_token(
                user.login_id, user.login_username, user.login_role
            )

            # Set tokens in cookies
            response = redirect("/home")  # Redirect instead of rendering

            response.set_cookie(
                settings.TOKENS["ACCESSTOKEN"],
                access_token,
                max_age=settings.TIME["ACCESS_TOKEN_MAX_AGE"],
                httponly=True,
            )
            response.set_cookie(
                settings.TOKENS["REFRESHTOKEN"],
                refresh_token,
                max_age=settings.TIME["REFRESH_TOKEN_MAX_AGE"],
                httponly=True,
            )

            # Optionally set user info in the session
            request.session["user_id"] = user.login_id
            request.session["username"] = user.login_username
            request.session["role"] = user.login_role

            return response

        except Exception as e:
            return render(request, "admin/login&register/login.html", {"error": str(e)})

    return redirect("admin_load_login")


def logout_view(request):
    """Handle user logout securely."""
    # First invalidate the session
    logout(request)

    # Then clear cookies
    response = redirect("admin_load_login")
    response.delete_cookie(settings.TOKENS["ACCESSTOKEN"])
    response.delete_cookie(settings.TOKENS["REFRESHTOKEN"])

    return response
