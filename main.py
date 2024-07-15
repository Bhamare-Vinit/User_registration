import re
# user_first_name=input("Enter your first name: ")
# user_fname=re.match("^[A-Z][a-z]{2,}$",user_first_name)
# print(user_fname)
# if user_fname:
#     print("Valid Firstname")
# else:
#     print("Invalid Firstname")

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

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email: ")
number=input("Enter your mobile number with country code: ")

if(check_if_valid_firstname(first_name,last_name) and check_if_valid_email(email) and check_if_valid_number(number)):
    print("Valid user input")
else:
    print("Invalid user input")