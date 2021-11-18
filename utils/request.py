from dataclasses import dataclass

import requests
from requests.api import request


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict


class APIRequest:
    def get(self, base_url,country,zipcode):
        request_url = base_url+'/'+country+'/'+'/'+zipcode;
        response = requests.get(request_url)
        return self.__get_responses(response)

    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers

        return Response(
            status_code, text, as_dict, headers
        )
