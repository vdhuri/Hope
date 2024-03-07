from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def home(request):
    users=User.objects.all()
    print(users)
    response_data=""
    for item in users:
        response_data += f"Email: {item.email}, Password: {item.password}\n"
    return HttpResponse(response_data)