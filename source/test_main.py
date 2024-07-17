import pytest
from main import (
    check_if_valid_firstname_lastname,
    check_if_valid_email,
    check_if_valid_number,
    check_if_valid_password,
)

def test_check_if_valid_firstname_lastname():
    assert check_if_valid_firstname_lastname("Vinit", "Bhamare") == True
    assert check_if_valid_firstname_lastname("vinit", "Bhamare") == False
    assert check_if_valid_firstname_lastname("Vinit", "bhamare") == False
    assert check_if_valid_firstname_lastname("Om", "Bhamare") == False
    assert check_if_valid_firstname_lastname("Vinit", "Om") == False
    assert check_if_valid_firstname_lastname("om", "bhamare") == False
    assert check_if_valid_firstname_lastname("vinit", "om") == False

def test_check_if_valid_email():
    assert check_if_valid_email("vinitbhamare2002@gmail.com") == True
    assert check_if_valid_email("vinitbhamare2002.gmail.com") == False
    assert check_if_valid_email("vinit@.com") == False
    assert check_if_valid_email("vinitbhamare@com") == False
    assert check_if_valid_email("vinitbhamare2002@gmail.c") == False

def test_check_if_valid_number():
    assert check_if_valid_number("91 8421558990") == True
    assert check_if_valid_number("918421558990") == False
    assert check_if_valid_number("91 842155899") == False
    assert check_if_valid_number("91 84215589901") == False
    assert check_if_valid_number("12 8421558990") == True

def test_check_if_valid_password():
    assert check_if_valid_password("Vinit@2002") == True
    assert check_if_valid_password("viniT@2002") == True
    assert check_if_valid_password("vinit@2002") == False
    assert check_if_valid_password("VINIT@2002") == False
    assert check_if_valid_password("vinit@om") == False
    assert check_if_valid_password("vInit2002") == False
    assert check_if_valid_password("Om@31") == False

if __name__ == "__main__":
    pytest.main()
