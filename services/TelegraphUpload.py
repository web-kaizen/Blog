from rest_framework.views import APIView

from services.CustomRoute import TelegraphEditRoute


class TelegraphUpload(TelegraphEditRoute, APIView):
    def get_method(self) -> str:
        return 'POST'

    def get_path(self) -> str:
        return '/upload'
