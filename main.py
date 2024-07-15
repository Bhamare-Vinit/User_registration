import re
# user_first_name=input("Enter your first name: ")
# user_fname=re.match("^[A-Z][a-z]{2,}$",user_first_name)
# print(user_fname)
# if user_fname:
#     print("Valid Firstname")
# else:
#     print("Invalid Firstname")

def check_if_valid_firstname(first_name):
    if re.search("[A-Z][a-z]{2,}$", first_name):
        return True
    else:
        return False


first_name = input("Enter your first name: ")

if(check_if_valid_firstname(first_name)):
    print("Valid first name")
else:
    print("Invalid first name")