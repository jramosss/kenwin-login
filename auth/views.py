from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpRequest
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import ValidationError, AuthenticationFailed


@api_view(["GET", "POST"])
def login(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        serializer = TokenObtainPairSerializer(data={"username": username, "password": password})
        try:
            serializer.is_valid()
        except (AuthenticationFailed, ValidationError) as e:
            return render(request, "login.html", {"error": e.detail})
        else:
            return render(request, "home.html", {"user_validated": True})
    else:
        return render(request, "login.html")


@api_view(["POST"])
def logout(request: HttpRequest):
    return render(request, "login.html")
