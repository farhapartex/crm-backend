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

class LoginAPIView(views.APIView):
    def validation(self, data):
        error_message = {}
        if "client_id" not in data:
            error_message["client_id"] = "client_id not found"
        
        if "client_secret" not in data:
            error_message["client_secret"] = "client_secret not found"
        
        if "grant_type" not in data:
            error_message["grant_type"] = "grant_type not found"
        
        if "grant_type" in data and data["grant_type"] != "password":
            error_message["grant_type"] = "Invalid grant_type"
        
        if "username" not in data:
            error_message["username"] = "username not found"
        
        if "password" not in data:
            error_message["password"] = "password not found"
        
        return error_message


    
    def post(self, request, *args, **kwargs):
        data = request.data
        
        error_message = self.validation(data)
        if bool(error_message):
            return Response(data=error_message, status=status.HTTP_404_NOT_FOUND)

        application = Token.get_client_application(data["client_id"], data["client_secret"])

        if application is None:
            return Response(data={"description": "Invalid client_id & client_secret", "success": False}, status=status.HTTP_404_NOT_FOUND)
        
        user = authenticate(request, username=data["username"], password=data["password"])

        if user is None:
            return Response(data={"description": "User not found", "success": False}, status=status.HTTP_404_NOT_FOUND)

        response, token_json = Token.create_token_response(user, data)

        if response is False:
            return Response(data={"description": token_json, "success": False}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(data=token_json, status=status.HTTP_200_OK)

