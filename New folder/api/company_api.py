"""
API для работы с компаниями.

Содержит класс CompanyApi для управления компаниями.
"""

from typing import Dict, Any, Optional
import requests
from api.client import ApiClient
from models.company import Company


class CompanyApi(ApiClient):
    """Класс для работы с API компаний."""

    def create_company(self, company_data: Dict[str, Any]) -> requests.Response:
        """
        Создает новую компанию.

        Args:
            company_data: Данные компании

        Returns:
            requests.Response: Ответ от сервера
        """
        return self.post("/company/create", company_data)

    def get_company_list(self) -> requests.Response:
        """
        Получает список всех компаний.

        Returns:
            requests.Response: Ответ от сервера
        """
        return self.get("/company/list")

    def get_company(self, company_id: int) -> requests.Response:
        """
        Получает информацию о компании по ID.

        Args:
            company_id: ID компании

        Returns:
            requests.Response: Ответ от сервера
        """
        return self.get(f"/company/{company_id}")

    def create_test_company(self) -> Company:
        """
        Создает тестовую компанию.

        Returns:
            Company: Созданная компания

        Raises:
            Exception: Если не удалось создать компанию
        """
        import time

        timestamp = int(time.time())
        company_data = {
            "name": f"Test Company {timestamp}",
            "description": "Created for automated testing"
        }

        response = self.create_company(company_data)

        if response.status_code == 201:
            return Company.from_response(response.json())
        else:
            raise Exception(f"Failed to create company: {response.status_code}")

    def get_valid_company_id(self) -> int:
        """
        Получает существующий ID компании (создает новую при необходимости).

        Returns:
            int: ID компании
        """
        try:
            company = self.create_test_company()
            return company.company_id
        except Exception:
            return 1