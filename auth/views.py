from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.http import HttpRequest
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import ValidationError


@api_view(["GET", "POST"])
def login(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        serializer = TokenObtainPairSerializer(data={"username": username, "password": password})
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return render(request, "login.html", {"error": e.detail})
        else:
            return redirect("/")
    else:
        return render(request, "login.html")
