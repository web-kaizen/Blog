from rest_framework.views import APIView

from services.CustomRoute import TelegraphUploadRoute


class TelegraphUpload(TelegraphUploadRoute, APIView):
    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/upload"
