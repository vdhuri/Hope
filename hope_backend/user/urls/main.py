from django.urls import re_path
from user.views import LoginView

urlpatterns=[
    re_path(r"login/$",LoginView.as_view())
]