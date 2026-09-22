import pytest

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.product_page import ProductPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage

AD_DOMAINS = [
    "**doubleclick.net**",
    "**googlesyndication.com**",
    "**googleadservices.com**",
]


@pytest.fixture(autouse=True)
def block_ads(context):
    for pattern in AD_DOMAINS:
        context.route(pattern, lambda route: route.abort())
    yield


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def registration_page(page):
    return RegistrationPage(page)


@pytest.fixture
def product_page(page):
    return ProductPage(page)


@pytest.fixture
def product_detail_page(page):
    return ProductDetailPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


@pytest.fixture
def payment_page(page):
    return PaymentPage(page)