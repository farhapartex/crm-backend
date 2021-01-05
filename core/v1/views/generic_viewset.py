from rest_framework import viewsets, status
from rest_framework.response import Response


class GenericViewset(viewsets.ModelViewSet):
    lookup_field = "uid"

    def get_queryset(self):
        return self.queryset.filter(is_deleted=False)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer_data = self.get_serializer(instance)
        return Response(data={"data":serializer_data.data, "success": True}, status=status.HTTP_200_OK)