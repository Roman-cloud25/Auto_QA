"""
Basic client for working with the API.
"""

import requests
from typing import Dict, Any, Optional
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config


class ApiClient:

    def __init__(self, base_url: Optional[str] = None):
        self.base_url = base_url or Config.BASE_URL
        self.session = requests.Session()
        self.session.headers.update(Config.HEADERS)

    def _get_auth_data(self) -> Dict[str, str]:
        return {
            "username": Config.AUTH_USERNAME,
            "password": Config.AUTH_PASSWORD
        }

    def _add_auth(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return {**data, **self._get_auth_data()}

    def get(self, endpoint: str, params: Optional[Dict] = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        if params:
            params = {**params, **self._get_auth_data()}
        else:
            params = self._get_auth_data()

        return self.session.get(url, params=params, timeout=Config.DEFAULT_TIMEOUT)

    def post(self, endpoint: str, data: Dict[str, Any]) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        data_with_auth = self._add_auth(data)

        return self.session.post(
            url,
            json=data_with_auth,
            timeout=Config.DEFAULT_TIMEOUT
        )

    def patch(self, endpoint: str, data: Dict[str, Any]) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        data_with_auth = self._add_auth(data)

        return self.session.patch(
            url,
            json=data_with_auth,
            timeout=Config.DEFAULT_TIMEOUT
        )