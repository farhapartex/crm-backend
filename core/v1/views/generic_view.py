from rest_framework import views, status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response


class GenericAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    def get_queryset(self):
        return self.queryset.filter(is_deleted=False)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer_data = self.get_serializer(queryset, many=True)
        return Response(data={"data": serializer_data.data, "success": True}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        queryset = self.list(request, *args, **kwargs)
        return queryset