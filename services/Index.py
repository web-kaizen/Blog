from django.shortcuts import render
from django.views import View

from core.Route import Route


class Index(Route, View):
    def get_method(self) -> str:
        return "GET"

    def get(self, request):
        template_name = 'index.html'
        return render(template_name=template_name, request=request)
