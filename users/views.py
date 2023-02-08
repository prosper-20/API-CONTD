from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer


@api_view(["POST"])
def api_register_view(request):
    if request.method == "POST":
        serilaizer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serilaizer.is_valid():
            user = serilaizer.save()
            data["Success"] = "Account creation successful"
            data["username"] = user.username
            data["email"] = user.email
            token = Token.objects.get(user=user).key
            data["token"] = token

            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)
