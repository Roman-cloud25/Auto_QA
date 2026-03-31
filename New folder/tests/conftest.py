"""
Фикстуры pytest для тестирования API.
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.employee_api import EmployeeApi
from api.company_api import CompanyApi
from utils.helpers import create_test_employee_data


@pytest.fixture(scope="session")
def api_client():
    """
    Фикстура для создания клиента API сотрудников.

    Returns:
        EmployeeApi: Клиент API
    """
    client = EmployeeApi()
    yield client


@pytest.fixture(scope="session")
def company_api():
    """
    Фикстура для создания клиента API компаний.

    Returns:
        CompanyApi: Клиент API компаний
    """
    client = CompanyApi()
    yield client


@pytest.fixture
def test_company(company_api):
    """
    Фикстура для создания тестовой компании.

    Returns:
        Company: Тестовая компания
    """
    company = company_api.create_test_company()
    yield company


@pytest.fixture
def test_employee(api_client):
    """
    Фикстура для создания тестового сотрудника.

    Returns:
        Employee: Тестовый сотрудник
    """
    employee = api_client.create_test_employee()
    yield employee


@pytest.fixture
def sample_employee_data(api_client):
    """
    Фикстура с примером данных сотрудника.

    Returns:
        Dict[str, Any]: Данные сотрудника
    """
    company_id = api_client.get_valid_company_id()
    return create_test_employee_data(company_id)


@pytest.fixture
def sample_update_data():
    """
    Фикстура с примером данных для обновления.

    Returns:
        Dict[str, Any]: Данные для обновления
    """
    return {
        "position": "Senior Software Engineer",
        "salary": 90000,
        "department": "R&D",
        "phone": "+79998887766"
    }