# Employee Management API Tests

Automated API tests for Employee Management System built with **pytest + requests** using the **API Client Model** pattern.

## What's tested

Employee CRUD operations: create → get → update → validate | **11 test scenarios**

## Stack

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Requests](https://img.shields.io/badge/Requests-2.31-green)
![pytest](https://img.shields.io/badge/pytest-7.4-orange)

## Project structure

```
├── api/
│ ├── client.py # Base HTTP client
│ ├── employee_api.py # Employee endpoints
│ └── company_api.py # Company endpoints
├── models/
│ ├── employee.py # Employee data model
│ └── company.py # Company data model
├── tests/
│ ├── conftest.py # Pytest fixtures
│ └── test_employee_api.py # Test scenarios
├── utils/
│ ├── helpers.py # Helper functions
│ └── validators.py # Response validators
├── config.py # Configuration
├── .env.example # Environment variables template
└── requirements.txt # Dependencies
```

## Setup

```bash
cd API_employee 
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
pytest tests/ -v
```