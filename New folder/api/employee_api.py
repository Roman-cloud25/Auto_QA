"""
API для работы с сотрудниками.

Содержит класс EmployeeApi для управления сотрудниками.
"""

from typing import Dict, Any, Optional, List
import time
import random
import requests
from api.client import ApiClient
from api.company_api import CompanyApi
from models.employee import Employee


class EmployeeApi(ApiClient):
    """Класс для работы с API сотрудников."""

    def __init__(self, base_url: Optional[str] = None):
        """Инициализирует API для работы с сотрудниками."""
        super().__init__(base_url)
        self.company_api = CompanyApi(base_url)
        self._company_id_cache = None

    def create_employee(self, employee_data: Dict[str, Any]) -> requests.Response:
        """
        Создает нового сотрудника.

        Args:
            employee_data: Данные сотрудника

        Returns:
            requests.Response: Ответ от сервера
        """
        return self.post("/employee/create", employee_data)

    def get_employee_info(self, employee_id: int) -> requests.Response:
        """
        Получает информацию о сотруднике по ID.

        Args:
            employee_id: ID сотрудника

        Returns:
            requests.Response: Ответ от сервера
        """
        return self.get("/employee/info", params={"id": employee_id})

    def change_employee(self, employee_id: int, change_data: Dict[str, Any]) -> requests.Response:
        """
        Изменяет данные сотрудника.

        Args:
            employee_id: ID сотрудника
            change_data: Данные для изменения

        Returns:
            requests.Response: Ответ от сервера
        """
        data = {"id": employee_id, **change_data}
        return self.patch("/employee/change", data)

    def get_valid_company_id(self) -> int:
        """
        Получает существующий ID компании.

        Returns:
            int: ID компании
        """
        if self._company_id_cache:
            return self._company_id_cache

        try:
            company_id = self.company_api.get_valid_company_id()
            self._company_id_cache = company_id
            return company_id
        except Exception:
            return 1

    def create_test_employee(self, custom_data: Optional[Dict] = None) -> Employee:
        """
        Создает тестового сотрудника.

        Args:
            custom_data: Пользовательские данные для переопределения

        Returns:
            Employee: Созданный сотрудник

        Raises:
            Exception: Если не удалось создать сотрудника
        """
        timestamp = int(time.time())
        random_suffix = random.randint(1000, 9999)

        company_id = self.get_valid_company_id()

        employee = Employee(
            first_name=f"Test{timestamp}",
            last_name=f"User{random_suffix}",
            email=f"test.user.{timestamp}.{random_suffix}@example.com",
            phone=f"+7{random.randint(9000000000, 9999999999)}",
            company_id=company_id,
            position="QA Engineer",
            department="Quality Assurance",
            salary=50000,
            address="Test Address",
            city="Test City"
        )

        if custom_data:
            for key, value in custom_data.items():
                if hasattr(employee, key):
                    setattr(employee, key, value)

        response = self.create_employee(employee.to_dict())

        if response.status_code == 200:
            return Employee.from_response(response.json())
        else:
            raise Exception(f"Failed to create employee: {response.status_code}")

    def create_employee_with_minimal_data(self) -> Employee:
        """
        Создает сотрудника только с обязательными полями.

        Returns:
            Employee: Созданный сотрудник
        """
        timestamp = int(time.time())
        company_id = self.get_valid_company_id()

        employee = Employee(
            first_name=f"Minimal{timestamp}",
            last_name="User",
            email=f"minimal.{timestamp}@example.com",
            phone=f"+7{random.randint(9000000000, 9999999999)}",
            company_id=company_id
        )

        response = self.create_employee(employee.to_dict())

        if response.status_code == 200:
            return Employee.from_response(response.json())
        else:
            raise Exception(f"Failed to create minimal employee: {response.status_code}")