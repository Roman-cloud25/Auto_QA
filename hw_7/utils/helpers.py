"""
Helper functions for tests.
"""

import time
import random
from typing import Dict, Any, Optional
from models.employee import Employee


def generate_unique_email(prefix: str = "test") -> str:
    timestamp = int(time.time())
    random_suffix = random.randint(1000, 9999)
    return f"{prefix}.{timestamp}.{random_suffix}@example.com"


def generate_unique_phone() -> str:
    return f"+7{random.randint(9000000000, 9999999999)}"


def create_test_employee_data(
        company_id: int,
        custom_data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    timestamp = int(time.time())

    employee_data = {
        "first_name": f"John{timestamp}",
        "last_name": "Doe",
        "email": generate_unique_email("john.doe"),
        "phone": generate_unique_phone(),
        "company_id": company_id,
        "position": "Software Engineer",
        "department": "Engineering",
        "salary": 75000
    }

    if custom_data:
        employee_data.update(custom_data)

    return employee_data


def create_test_company_data() -> Dict[str, Any]:
    timestamp = int(time.time())

    return {
        "name": f"Test Company {timestamp}",
        "description": "Created for automated testing"
    }