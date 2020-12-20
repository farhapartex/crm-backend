from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import status, generics, views, viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from core.v1.permissions.is_admin_user_permission import IS_ADMIN_USER
from rest_framework.response import Response
from core.models.auth.role import Role
from core.v1.serializers.auth.role_serializer import RoleSerializer


class RoleAPIView(views.APIView):
    permission_classes = (IsAuthenticated, IS_ADMIN_USER,)

    def get(self, request, *args, **kwargs):
        user = request.user
        roles = Role.objects.all()
        serializer_data = RoleSerializer(roles, many=True).data
        return Response(data={"data":serializer_data, "success": True}, status=status.HTTP_200_OK)







