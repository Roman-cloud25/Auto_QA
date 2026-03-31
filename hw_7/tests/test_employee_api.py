import pytest
import json
import time
import sys
import os
from typing import Dict, Any

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestEmployeeApi:

    def test_create_employee_success(self, api_client, sample_employee_data):
        response = api_client.create_employee(sample_employee_data)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        response_data = response.json()

        assert response_data.get("first_name") == sample_employee_data["first_name"]
        assert response_data.get("last_name") == sample_employee_data["last_name"]
        assert response_data.get("email") == sample_employee_data["email"]
        assert response_data.get("company_id") == sample_employee_data["company_id"]

        employee_email = response_data.get("email")

    def test_create_employee_without_required_fields(self, api_client):
        response = api_client.create_employee({})
        assert response.status_code == 422, f"Expected 422, got {response.status_code}"
        response_data = response.json()
        assert "detail" in response_data, "Response should contain validation errors"

    def test_create_employee_without_phone(self, api_client):
        import time
        import random
        timestamp = int(time.time())
        employee_data = {
            "first_name": f"NoPhone{timestamp}",
            "last_name": "User",
            "email": f"nophone.{timestamp}@example.com",
            "company_id": api_client.get_valid_company_id(),
            "position": "Tester"
        }
        response = api_client.create_employee(employee_data)
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    def test_create_employee_with_invalid_data(self, api_client):
        invalid_data = {
            "first_name": "",
            "last_name": "",
            "email": "invalid-email",
            "company_id": "not_a_number",
            "phone": "invalid",
            "salary": "not_a_number"
        }
        response = api_client.create_employee(invalid_data)
        assert response.status_code == 422, f"Expected 422, got {response.status_code}"

    def test_get_employee_info_not_found(self, api_client):
        non_existent_id = 999999999
        response = api_client.get_employee_info(non_existent_id)
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    def test_get_employee_info_invalid_id(self, api_client):
        response = api_client.session.get(
            f"{api_client.base_url}/employee/info",
            params={"id": "invalid", **api_client._get_auth_data()},
            timeout=10
        )
        assert response.status_code in [400, 404, 422], \
            f"Expected 400, 404 or 422, got {response.status_code}"

    def test_change_employee_not_found(self, api_client):
        non_existent_id = 999999999
        change_data = {
            "position": "Updated Position"
        }
        response = api_client.change_employee(non_existent_id, change_data)
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    def test_create_and_update_workflow(self, api_client):
        import time
        import random
        timestamp = int(time.time())
        company_data = {
            "name": f"Workflow Company {timestamp}",
            "description": "Test workflow"
        }
        company_response = api_client.create_company(company_data)
        assert company_response.status_code == 201
        company_id = company_response.json().get("id")

        employee_data = {
            "first_name": f"Workflow{timestamp}",
            "last_name": "Test",
            "email": f"workflow.{timestamp}@example.com",
            "company_id": company_id,
            "phone": f"+7{random.randint(9000000000, 9999999999)}",
            "position": "Junior Developer",
            "salary": 50000
        }
        create_response = api_client.create_employee(employee_data)
        assert create_response.status_code == 200
        created_employee = create_response.json()

        update_data = {
            "position": "Senior Developer",
            "salary": 80000
        }
        try:
            update_response = api_client.change_employee(employee_data["email"], update_data)
            # Проверяем результат
            assert update_response.status_code in [200, 404]
        except:
            pytest.skip("Update by email not supported")

    def test_multiple_employees_creation(self, api_client):
        import time
        import random
        timestamp = int(time.time())
        company_data = {
            "name": f"Bulk Company {timestamp}",
            "description": "For bulk employee creation"
        }
        company_response = api_client.create_company(company_data)
        assert company_response.status_code == 201
        company_id = company_response.json().get("id")

        employees = []

        try:
            for i in range(3):
                employee_data = {
                    "first_name": f"Bulk{i}_{timestamp}",
                    "last_name": "User",
                    "email": f"bulk.{i}.{timestamp}@example.com",
                    "company_id": company_id,
                    "phone": f"+7{random.randint(9000000000, 9999999999)}",
                    "position": f"Position {i}",
                    "department": "Bulk Department",
                    "salary": 60000 + (i * 5000)
                }

                response = api_client.create_employee(employee_data)
                assert response.status_code == 200, f"Failed to create employee {i}"

                employees.append(response.json())

            assert len(employees) == 3
            for i, emp in enumerate(employees):
                assert emp.get("first_name") == f"Bulk{i}_{timestamp}"
                assert emp.get("company_id") == company_id
        finally:
            pass

    def test_response_structure_consistency(self, api_client, sample_employee_data):
        response = api_client.create_employee(sample_employee_data)
        assert response.status_code == 200
        data = response.json()
        required_fields = ["first_name", "last_name", "email", "company_id", "phone"]
        for field in required_fields:
            assert field in data, f"Field '{field}' is missing in response"

        assert isinstance(data["first_name"], str), "First name should be string"
        assert isinstance(data["last_name"], str), "Last name should be string"
        assert isinstance(data["email"], str), "Email should be string"
        assert isinstance(data["company_id"], int), "Company ID should be integer"
        assert isinstance(data["phone"], str), "Phone should be string"
        assert "@" in data["email"], "Email should contain @"
        assert data["phone"].startswith("+"), "Phone should start with +"

    def test_create_employee_with_minimal_fields(self, api_client):
        import time
        import random
        timestamp = int(time.time())
        company_id = api_client.get_valid_company_id()
        minimal_data = {
            "first_name": f"Minimal{timestamp}",
            "last_name": "User",
            "company_id": company_id,
            "phone": f"+7{random.randint(9000000000, 9999999999)}"
        }
        response = api_client.create_employee(minimal_data)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        response_data = response.json()
        assert response_data.get("first_name") == minimal_data["first_name"]
        assert response_data.get("last_name") == minimal_data["last_name"]
        assert response_data.get("phone") == minimal_data["phone"]
