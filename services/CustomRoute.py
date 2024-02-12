import requests

from core.Route import Route
from core.settings import TELEGRAPH_URL, TELEGRAPH_EDIT_URL


class TelegraphEditRoute(Route):
    def __init__(self, need_execute_local=False, *args, **kwargs):
        self.TELEGRAPH_EDIT_URL = TELEGRAPH_EDIT_URL
        super().__init__(self, *args, **kwargs)

    def request_setter(self, request, *args, **kwargs):
        self.set_method(self.get_method())
        if self.get_method() == "GET" and request.query_params:
            query_params = '?' + '&'.join([f"{key}={value}" for key, value in request.query_params.items()])
            self.set_url(f'{self.TELEGRAPH_EDIT_URL}{self.get_path()}{query_params}')
        else:
            self.set_url(f'{self.TELEGRAPH_EDIT_URL}{self.get_path()}')

        self.set_headers({
            'Origin': 'https://telegra.ph',
            'Referer': 'https://telegra.ph/',
        })

        self.set_request(request.data)

    def send(self) -> tuple:
        response = requests.request(
            method=self.get_method(),
            url=self.get_url(),
            json=self.get_request(),
            headers=self.get_headers(),

        )
        try:
            response_body = response.json()
        except requests.JSONDecodeError as ex:
            response_body = response.text if response.text else None
        finally:
            response_headers = dict(response.headers)
            response_status_code = response.status_code

        #  filtered headers
        response_headers = {k: v for k, v in response_headers.items() if k not in self._not_allowed_headers}
        response_headers.update({
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        })

        self.set_response(response_body, response_headers, response_status_code)

        return self.get_response(), self.get_headers(), self._status_code


class TelegraphUploadRoute(Route):
    def __init__(self, need_execute_local=False, *args, **kwargs):
        self.TELEGRAPH_URL = TELEGRAPH_URL
        super().__init__(self, *args, **kwargs)

    def request_setter(self, request, *args, **kwargs):
        self.set_method(self.get_method())
        if self.get_method() == "GET" and request.query_params:
            query_params = '?' + '&'.join([f"{key}={value}" for key, value in request.query_params.items()])
            self.set_url(f'{self.TELEGRAPH_URL}{self.get_path()}{query_params}')
        else:
            self.set_url(f'{self.TELEGRAPH_URL}{self.get_path()}')

        self.set_headers({
            'Origin': 'https://telegra.ph',
            'Referer': 'https://telegra.ph/',
        })

        self.set_request(request.data)

    def send(self) -> tuple:
        response = requests.request(
            method=self.get_method(),
            url=self.get_url(),
            files=self.get_request(),
            headers=self.get_headers(),
        )
        try:
            response_body = response.json()
        except requests.JSONDecodeError as ex:
            response_body = response.text if response.text else None
        finally:
            response_headers = dict(response.headers)
            response_status_code = response.status_code

        #  filtered headers
        response_headers = {k: v for k, v in response_headers.items() if k not in self._not_allowed_headers}
        response_headers.update({
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        })

        self.set_response(response_body, response_headers, response_status_code)

        return self.get_response(), self.get_headers(), self._status_code