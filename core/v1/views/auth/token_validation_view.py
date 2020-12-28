from django.conf import settings
from rest_framework import status, generics, views, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.auth.token import Token


class TokenValidationView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        if "token" not in request.data or len(request.data["token"]) == 0:
            return Response(data={"message": "Token not found", "success": False}, status=status.HTTP_400_BAD_REQUEST)

        token = request.data["token"]
        is_token_valid = Token.is_token_valid(token)

        return Response(data={"data": {"is_token_valid": is_token_valid}, "success": True}, status=status.HTTP_200_OK)