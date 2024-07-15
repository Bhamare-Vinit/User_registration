import re

def check_if_valid_firstname(first_name,last_name):
    if re.search("[A-Z][a-z]{2,}$", first_name) and re.search("[A-Z][a-z]{2,}$", last_name):
        return True
    else:
        return False

def check_if_valid_email(email):
    if re.search(r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$", email):
        return True
    else:
        return False
    
def check_if_valid_number(number):
    if re.search(r"^\d{2}\s\d{10}$", number):
        return True
    else:
        return False

def check_if_valid_password(password):
    pattern=r"^(?=.*[!@#$%^&*()_+{}|:<>?])(?!.*[!@#$%^&*()_+{}|:<>?].*[!@#$%^&*()_+{}|:<>?]).*$"
    if  len(password)>=8:
        if re.search(r"[A-Z]",password) and re.search(r"\d",password) and re.search(r"[a-z]",password ) and re.search(pattern,password):
            return True
    else:
        return False
# ^.*(?=[]*[!@#$%^&*()_+{}|:<>?]).*$
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# email = input("Enter your email: ")
# number=input("Enter your mobile number with country code: ")
password=input("Enter your password: ")

# if(check_if_valid_firstname(first_name,last_name) and check_if_valid_email(email) and check_if_valid_number(number)
#     and check_if_valid_password(password)):
#     print("Valid user input")
# else:
#     print("Invalid user input")

if( check_if_valid_password(password)):
    print("Valid user input")
else:
    print("Invalid user input")