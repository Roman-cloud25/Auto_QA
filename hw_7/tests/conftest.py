"""
Pytest fixtures for API testing.
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
    client = EmployeeApi()
    yield client


@pytest.fixture(scope="session")
def company_api():
    client = CompanyApi()
    yield client


@pytest.fixture
def test_company(company_api):
    company = company_api.create_test_company()
    yield company


@pytest.fixture
def test_employee(api_client):
    employee = api_client.create_test_employee()
    yield employee


@pytest.fixture
def sample_employee_data(api_client):
    company_id = api_client.get_valid_company_id()
    return create_test_employee_data(company_id)


@pytest.fixture
def sample_update_data():
    return {
        "position": "Senior Software Engineer",
        "salary": 90000,
        "department": "R&D",
        "phone": "+79998887766"
    }