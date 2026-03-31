"""
Базовый клиент для работы с API.

Содержит базовый класс ApiClient для всех API запросов.
"""

import requests
from typing import Dict, Any, Optional
from config import Config


class ApiClient:
    """
    Базовый клиент для работы с API.

    Attributes:
        base_url: Базовый URL API
        session: Сессия requests для выполнения запросов
    """

    def __init__(self, base_url: Optional[str] = None):
        """
        Инициализация API клиента.

        Args:
            base_url: Базовый URL API (опционально)
        """
        self.base_url = base_url or Config.BASE_URL
        self.session = requests.Session()
        self.session.headers.update(Config.HEADERS)

    def _get_auth_data(self) -> Dict[str, str]:
        """
        Получает данные для аутентификации.

        Returns:
            Dict[str, str]: Словарь с данными аутентификации
        """
        return {
            "username": Config.AUTH_USERNAME,
            "password": Config.AUTH_PASSWORD
        }

    def _add_auth(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Добавляет данные аутентификации к запросу.

        Args:
            data: Исходные данные запроса

        Returns:
            Dict[str, Any]: Данные с добавленной аутентификацией
        """
        return {**data, **self._get_auth_data()}

    def get(self, endpoint: str, params: Optional[Dict] = None) -> requests.Response:
        """
        Выполняет GET запрос.

        Args:
            endpoint: Endpoint API
            params: Параметры запроса

        Returns:
            requests.Response: Ответ от сервера
        """
        url = f"{self.base_url}{endpoint}"
        if params:
            params = {**params, **self._get_auth_data()}
        else:
            params = self._get_auth_data()

        return self.session.get(url, params=params, timeout=Config.DEFAULT_TIMEOUT)

    def post(self, endpoint: str, data: Dict[str, Any]) -> requests.Response:
        """
        Выполняет POST запрос.

        Args:
            endpoint: Endpoint API
            data: Данные для отправки

        Returns:
            requests.Response: Ответ от сервера
        """
        url = f"{self.base_url}{endpoint}"
        data_with_auth = self._add_auth(data)

        return self.session.post(
            url,
            json=data_with_auth,
            timeout=Config.DEFAULT_TIMEOUT
        )

    def patch(self, endpoint: str, data: Dict[str, Any]) -> requests.Response:
        """
        Выполняет PATCH запрос.

        Args:
            endpoint: Endpoint API
            data: Данные для отправки

        Returns:
            requests.Response: Ответ от сервера
        """
        url = f"{self.base_url}{endpoint}"
        data_with_auth = self._add_auth(data)

        return self.session.patch(
            url,
            json=data_with_auth,
            timeout=Config.DEFAULT_TIMEOUT
        )