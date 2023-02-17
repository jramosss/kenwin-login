import pytest
from django.test import Client
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


client = Client()


pytestmark = pytest.mark.django_db


def test_show_login_form():
    response = client.get("/auth/login/")
    assert response.status_code == 200


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


@pytest.mark.parametrize("user_logged_in", [True, False])
def test_logout(user_logged_in):
    if user_logged_in:
        user = mixer.blend(User)
        client.force_login(user)
    response = client.get("/auth/logout/")
    assert response.status_code == 200
