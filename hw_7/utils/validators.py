"""
Functions for validating API responses.
"""
from typing import Dict, Any, List


def validate_employee_response(data: Dict[str, Any]) -> bool:
    required_fields = ["first_name", "last_name", "email", "company_id", "phone"]

    for field in required_fields:
        if field not in data:
            return False

    if not isinstance(data["first_name"], str):
        return False
    if not isinstance(data["last_name"], str):
        return False
    if not isinstance(data["email"], str) or "@" not in data["email"]:
        return False
    if not isinstance(data["company_id"], int):
        return False
    if not isinstance(data["phone"], str) or not data["phone"].startswith("+"):
        return False

    return True


def validate_company_response(data: Dict[str, Any]) -> bool:
    required_fields = ["name", "description", "is_active"]

    for field in required_fields:
        if field not in data:
            return False

    return True


def validate_error_response(data: Dict[str, Any]) -> bool:
    return "detail" in data