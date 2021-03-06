from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.v1.serializers.status_change_serializer import StatusChangeSerializer
from core.utils import load_model


class StatusChangeAPIView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer_data = StatusChangeSerializer(data=data)
        if serializer_data.is_valid():
            context = data["context"]
            uid = data["uid"]
            ModelClass = load_model(context)

            model_object = ModelClass.objects.filter(uid=uid, is_deleted=False).first()
            if model_object is None:
                response = "Data not found"
                status_code = 400
            else:
                model_object.change_status()
                response = "Data status changes successfully"
                status_code = 200

            return Response(data={"data": response, "success": True if status_code == 200 else False}, status=status_code)
