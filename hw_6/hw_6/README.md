# SauceDemo E2E Tests

Automated end-to-end tests for [saucedemo.com](https://www.saucedemo.com) built with **Selenium + pytest** using the **Page Object Model** pattern.

## What's tested

Add 3 items to cart → checkout → verify total | `$58.29`

## Stack

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green)
![pytest](https://img.shields.io/badge/pytest-9.x-orange)

## Project structure

```
├── pages/
│   ├── base_page.py               
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_step_one_page.py
│   └── checkout_step_two_page.py
├── tests/
│   └── test_checkout.py
├── conftest.py                    
├── pytest.ini
└── requirements.txt
```

## Setup

```bash
cd saucedemo-tests
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
pytest
```

