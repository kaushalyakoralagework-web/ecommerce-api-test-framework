# Ecommerce-api-test-framework

A production-style API test automation framework built in Python,
demonstrating real-world QA engineering practices across functional,
contract, integration, and UI smoke testing.

**Target application:** [Fake Store API](https://fakestoreapi.com) —
a fully functional e-commerce REST API.

---

## What this project demonstrates

- REST API test automation using `requests` and `pytest`
- Response schema validation using `Pydantic` models
- Multi-environment configuration via YAML
- End-to-end integration test flows across multiple endpoints
- UI smoke testing with `Playwright` (Python)
- CI/CD pipeline with GitHub Actions — tests run automatically on every PR
- HTML and Allure test reporting
- Clean framework architecture separating client, models, and test layers

---

## Tech stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| pytest | Test runner |
| requests | HTTP client |
| Pydantic v2 | Schema validation |
| Playwright | UI smoke testing |
| PyYAML | Environment configuration |
| pytest-html | HTML reporting |
| Allure | Advanced reporting |
| GitHub Actions | CI/CD pipeline |
| Faker | Test data generation |

---

## Project structure
ecommerce-api-test-framework/

├── src/

│   ├── clients/          # HTTP client layer (requests wrapper)

│   ├── models/           # Pydantic models for request/response

│   └── utils/            # Config loader, logger, helpers

├── tests/

│   ├── functional/       # Endpoint functional tests

│   ├── contract/         # Schema and contract validation

│   ├── integration/      # End-to-end chained flows

│   └── ui_smoke/         # Playwright smoke tests

├── config/

│   └── environments.yaml # Multi-environment configuration

├── reports/              # Generated test reports

├── .github/workflows/    # GitHub Actions CI pipeline

├── TEST_SCENARIOS.md     # Full test scenario documentation

├── pytest.ini            # pytest configuration

└── requirements.txt      # Project dependencies


---

## Test coverage

Full test scenario documentation is available in
[TEST_SCENARIOS.md](TEST_SCENARIOS.md)

| Area | Tests | Type |
|------|-------|------|
| Products API | 13 functional + 8 contract | GET, POST, PUT, PATCH, DELETE |
| Cart API | 12 functional + 5 contract | GET, POST, PUT, PATCH, DELETE |
| User API | 10 functional + 6 contract | GET, POST, PUT, PATCH, DELETE |
| Auth API | 6 functional + 3 contract | POST |
| Integration flows | 4 end-to-end | Multi-endpoint chained |
| UI Smoke | 4 scenarios | Playwright |

---

## Getting started

### Prerequisites
- Python 3.11+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/kaushalyakoralagework-web/ecommerce-api-test-framework.git
cd ecommerce-api-test-framework

# Create and activate virtual environment
python3.11 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser
playwright install chromium
```

### Running tests

```bash
# Run all tests
pytest

# Run specific test type
pytest -m functional
pytest -m contract
pytest -m integration
pytest -m smoke

# Run with Allure reporting
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

### Environment configuration

Tests run against `dev` environment by default.
To switch environments:

```bash
ENV=staging pytest
```

Configuration is managed in `config/environments.yaml`

---

## CI/CD

GitHub Actions pipeline runs automatically on:
- Every push to `feature/*` branches
- Every pull request to `main`

Pipeline steps:
1. Set up Python 3.11
2. Install dependencies
3. Install Playwright browsers
4. Run full test suite
5. Generate and upload HTML report as artifact

---

## Test results

Reports are generated in two formats:

**HTML report** — `reports/report.html`
Generated automatically on every test run.

**Allure report** — `reports/allure-results/`
```bash
allure serve reports/allure-results
```

---

## Author

**Kaushalya Koralage**
Senior QA Automation Engineer | ISTQB CTFL
[LinkedIn](https://www.linkedin.com/in/kaushalya-koralage) |
[GitHub](https://github.com/kaushalyakoralagework-web)# CI trigger
