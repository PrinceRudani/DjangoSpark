from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from login.models import LoginVO
from register.models import RegisterVO


def admin_load_register(request):
    return render(request, "admin/login&register/register.html")


def admin_insert_register(request):
    if request.method == "POST":
        try:
            # Collect data from the POST request
            register_firstname = request.POST.get("registerFirstname")
            register_lastname = request.POST.get("registerLastname")
            register_gender = request.POST.get("registerGender")
            register_email = request.POST.get("registerEmail")
            register_phone = request.POST.get("registerPhone")

            login_username = request.POST.get("registerUsername")
            login_password = request.POST.get("registerPassword")
            login_role = "USER"
            login_status = 0
            # Check if username already exists
            if LoginVO.objects.filter(login_username=login_username).exists():
                return render(
                    request,
                    "admin/login&register/register.html",
                    {"error": "Username already exists."},
                )

            # Create and save login details first
            login_vo = LoginVO(
                login_username=login_username,
                login_password=make_password(login_password),  # Hash
                # password before saving
                login_role=login_role,
                login_status=login_status,
            )
            login_vo.save()

            # Create and save register details
            register_vo = RegisterVO(
                register_firstname=register_firstname,
                register_lastname=register_lastname,
                register_gender=register_gender,
                register_email=register_email,
                register_phone=register_phone,
                register_login_vo=login_vo,  # Assign saved login instance
            )
            register_vo.save()

            return render(
                request,
                "admin/login&register/login.html",
                {"success": "Registration successful!"},
            )

        except Exception as e:
            return render(
                request,
                "admin/login&register/register.html",
                {"error": f"Error occurred: {str(e)}"},
            )

    return render(
        request,
        "admin/login&register/register.html",
        {"error": "Invalid request method."},
    )
