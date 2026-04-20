import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected_url,expected_error",
    [
        # valid login
        ("standard_user", "secret_sauce", "inventory", None),

        #Invalid login
        ("invalid_user", "wrong_password", None, "Username and password do not match"),

        # Edge casess
        ("' OR '1'='1", "anything", None, "Username and password do not match"),
        ("!@#$%^&*()", "!@#$%^&*()", None, "Username and password do not match"),
        ("STANDARD_USER", "SECRET_SAUCE", None, "Username and password do not match"),
        (" standard_user ", " secret_sauce ", None, "Username and password do not match"),
        ("a" * 1000, "b" * 1000, None, "Username and password do not match"),

        # empty fields
        ("", "secret_sauce", None, "Username is required"),
        ("standard_user", "", None, "Password is required"),
    ],
    ids=[
        "valid_login",
        "invalid_login",
        "sql_injection_attempt",
        "special_characters",
        "case_sensitivity_check",
        "leading_trailing_spaces",
        "long_input",
        "empty_username",
        "empty_password",
    ]
)
def test_login(driver, username, password, expected_url, expected_error):
    login_page = LoginPage(driver)
    login_page.load()

    login_page.login(username, password)

    if expected_url:
        login_page.wait_for_inventory()
        assert expected_url in login_page.get_url()
    else:
        error_text = login_page.get_error_message()
        assert expected_error in error_text