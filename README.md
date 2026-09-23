# Automation Exercise — Playwright + pytest Test Suite

Automation phase of a self-directed QA portfolio project. The manual phase (43 test cases across 9 functional suites, executed against [automationexercise.com](https://automationexercise.com)) is documented in full on the project's case-study page:

**📄 Full manual-phase case study: [damilareakanni.framer.website/projects/automation-exercise---qa](https://damilareakanni.framer.website/projects/automation-exercise---qa)**

This repository automates 15 of those 43 cases, selected for business risk and core-requirement coverage, using Playwright (Python), pytest, and the Page Object Model.

---

## Tech Stack

- **Playwright** (Python) — browser automation
- **pytest** + **pytest-playwright** — test framework and execution
- **Page Object Model** — one page object per distinct page/component
- **Allure** — test reporting
- **python-dotenv** — environment configuration

---

## Project Structure

```
AutomationExercise/
├── pages/                  # Page Object Model — one file per page/component
│   ├── base_page.py
│   ├── header_component.py
│   ├── login_page.py
│   ├── registration_page.py
│   ├── product_page.py
│   ├── product_detail_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── payment_page.py
├── tests/                  # 15 tests across 5 suites
│   ├── test_login.py
│   ├── test_registration.py
│   ├── test_product.py
│   ├── test_cart.py
│   └── test_checkout.py
├── config.py                # Loads .env into usable config values
├── conftest.py               # Fixtures + ad-blocking
├── pytest.ini                 # Marker registration
├── .gitgnore                 # Excludes .env, caches, and generated report folders from git
├── .env.example                 # Template for required environment variables
└── requirements.txt
```

---

## Setup

```bash
git clone https://github.com/sammyx-14/AutomationExercise-Project.git
cd AutomationExercise-Project

python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

pip install -r requirements.txt
playwright install

cp .env.example .env
```

### Test account

Fill in `.env` with a registered account on automationexercise.com. For convenience, this demo account is safe to use as-is (this is a public QA practice site — no real data, no sensitivity):

```
TEST_USER_NAME=Demo Tester
TEST_USER_EMAIL=demo.tester@example.com
TEST_USER_PASSWORD=DemoTester123
```
`.env` is gitignored and never committed — only `.env.example` (a blank template) is tracked. This isn't just convention: this site's "Delete Account" has no confirmation step, so a leaked credential could let anyone delete the fixture account this suite depends on.

---

## Running the Tests

Run everything:
```bash
pytest tests/ -v
```

Run one suite:
```bash
pytest tests/test_login.py -v
```

Run by marker (e.g. only cart tests):
```bash
pytest -m cart -v
```
Available markers: `login`, `logout`, `registration`, `product`, `cart`, `checkout`, `payment`.

Watch a test run in a real browser:
```bash
pytest tests/test_login.py --headed --slowmo 1000
```

---

## Test Report (Allure)

```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

This opens an interactive HTML report — pass/fail breakdown, per-test timing, and step-level detail for all 15 tests.

---

## Scope

15 of the original 43 manual test cases were selected for automation, covering the core account, product, cart, and checkout/payment flows. Full selection rationale is documented in the case study linked above.

| Suite | Cases |
|---|---|
| Login/Logout | TC-LOGIN-001, 002, 003, 006 |
| Registration | TC-REG-001, 002 |
| Product Discovery | TC-PROD-001, 003 |
| Cart | TC-CART-001, 002, 004, TC-CHK-002 |
| Checkout/Payment | TC-CHK-004, 008, TC-PAY-003 |

## Known Site Behavior

A few confirmed, permanent behaviors on this demo site (not bugs in this test suite) that the tests are deliberately written around:

- Cart quantity is not editable — it's a disabled counter, incremented only by adding the same product again.
- Checkout for an empty cart shows a message rather than a disabled button.
- Payment fields accept any input, including non-numeric characters — no format validation, and orders complete regardless.
- Account deletion has no confirmation step.

---

Built by Damilare A.
