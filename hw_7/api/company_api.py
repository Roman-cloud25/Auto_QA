"""
API for working with companies.
"""

from typing import Dict, Any, Optional
import requests
from api.client import ApiClient
from models.company import Company


class CompanyApi(ApiClient):

    def create_company(self, company_data: Dict[str, Any]) -> requests.Response:
         return self.post("/company/create", company_data)

    def get_company_list(self) -> requests.Response:
        return self.get("/company/list")

    def get_company(self, company_id: int) -> requests.Response:
         return self.get(f"/company/{company_id}")

    def create_test_company(self) -> Company:
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
        try:
            company = self.create_test_company()
            return company.company_id
        except Exception:
            return 1