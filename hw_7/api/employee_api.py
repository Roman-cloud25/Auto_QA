"""
API for working with employees.
"""
import time
import random
from typing import Dict, Any, Optional
import requests
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.client import ApiClient
from models.employee import Employee


class EmployeeApi(ApiClient):

    def __init__(self, base_url: Optional[str] = None):
        super().__init__(base_url)
        self._company_id_cache = None

    def create_company(self, company_data: Dict[str, Any]) -> requests.Response:
        return self.post("/company/create", company_data)

    def get_company_list(self) -> requests.Response:
        return self.get("/company/list")

    def create_employee(self, employee_data: Dict[str, Any]) -> requests.Response:
        return self.post("/employee/create", employee_data)

    def get_employee_info(self, employee_id: int) -> requests.Response:
        return self.get("/employee/info", params={"id": employee_id})

    def change_employee(self, employee_id: int, change_data: Dict[str, Any]) -> requests.Response:
        data = {"id": employee_id, **change_data}
        return self.patch("/employee/change", data)

    def get_valid_company_id(self) -> int:
        if self._company_id_cache:
            return self._company_id_cache

        try:
            company = self.create_test_company()
            self._company_id_cache = company.get("id")
            return self._company_id_cache
        except Exception:
            return 1

    def create_test_company(self) -> Dict[str, Any]:
        timestamp = int(time.time())
        company_data = {
            "name": f"Test Company {timestamp}",
            "description": "Created for automated testing"
        }
        response = self.create_company(company_data)

        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to create company: {response.status_code}")

    def create_test_employee(self, custom_data: Optional[Dict] = None) -> Employee:
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