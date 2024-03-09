from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
from django.contrib.auth.models import User
from response import response_wrapper


class LoginView(APIView):
    @response_wrapper#this is a decorater
    def get(self, request, response, format=None):
        users=User.objects.all()
        data=[]
        for user in users:
            data.append({"first_name":user.first_name})
        response=data
        
