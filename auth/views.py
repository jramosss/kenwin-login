import json
from django.shortcuts import render
from django.http import HttpRequest
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import ValidationError, AuthenticationFailed


def login(request: HttpRequest):
    if request.method == "POST":
        params = request.POST or json.loads(request.body)
        username = params.get("username")
        password = params.get("password")
        serializer = TokenObtainPairSerializer(data={"username": username, "password": password})
        try:
            serializer.is_valid(raise_exception=True)
        except (AuthenticationFailed, ValidationError) as e:
            return render(request, "login.html", {"error": e.detail}, status=400)
        else:
            return render(request, "home.html", {"user_validated": True})
    else:
        return render(request, "login.html")


def logout(request: HttpRequest):
    return render(request, "login.html")
