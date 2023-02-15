import pytest
from django.test import Client
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


client = Client()


pytestmark = pytest.mark.django_db


def test_login_success():
    user_data = {"username": "test", "password": "test"}
    mixer.blend(User, username=user_data["username"], password=make_password(user_data["password"]))
    response = client.post("/auth/login/", user_data, content_type="application/json")
    assert response.status_code == 200
    assert response.context["user_validated"] is True


def test_login_fail():
    user_data = {"username": "test", "password": "test"}
    response = client.post("/auth/login/", user_data, content_type="application/json")
    assert response.status_code == 400
    assert response.context["error"] == "No active account found with the given credentials"


def test_logout():
    response = client.get("/auth/logout/")
    assert response.status_code == 200
