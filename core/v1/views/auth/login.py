from django.conf import settings
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from rest_framework import status, generics, views, viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from core.models.auth.user import User
from core.auth.token import Token
from core.v1.serializers.auth.TokenSerializer import TokenSerializer


class LoginAPIView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = TokenSerializer(data=data)
        if serializer.is_valid():
            application = Token.get_client_application(data["client_id"], data["client_secret"])
            if application is None:
                return Response(data={"description": "Invalid client_id & client_secret", "success": False},
                                status=status.HTTP_404_NOT_FOUND)
            user = authenticate(request, username=data["username"], password=data["password"])
            if user is None:
                return Response(data={"description": "User not found", "success": False},
                                status=status.HTTP_404_NOT_FOUND)
            response, token_json = Token.create_token_response(user, data)
            if response is False:
                return Response(data={"description": token_json, "success": False}, status=status.HTTP_404_NOT_FOUND)
            return Response(data=token_json, status=status.HTTP_200_OK)
        else:
            return Response(data={"description": "Invalid data", "success": False}, status=status.HTTP_400_BAD_REQUEST)



        


