import re

def check_if_valid_firstname_lastname(first_name, last_name):
    try:
        if re.search("[A-Z][a-z]{2,}$", first_name) and re.search("[A-Z][a-z]{2,}$", last_name):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error validating first name and last name: {e}")
        return False

def check_if_valid_email(email):
    try:
        if re.search(r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$", email):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error validating email: {e}")
        return False

def check_if_valid_number(number):
    try:
        if re.search(r"^\d{2}\s\d{10}$", number):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error validating number: {e}")
        return False

def check_if_valid_password(password):
    try:
        pattern = r"^(?=.*[!@#$%^&*()_+{}|:<>?])(?!.*[!@#$%^&*()_+{}|:<>?].*[!@#$%^&*()_+{}|:<>?]).*$"
        if len(password) >= 8:
            if re.search(r"[A-Z]", password) and re.search(r"\d", password) and re.search(r"[a-z]", password) and re.search(pattern, password):
                
                return True
            else:
                print("Bad password: Missing required characters")
                return False
        else:
            print("Bad password: Too short")
            return False
    except Exception as e:
        print(f"Error validating password: {e}")
        return False

if __name__ == "__main__":
    try:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email: ")
        number = input("Enter your mobile number with country code: ")
        password = input("Enter your password: ")

        if (check_if_valid_firstname_lastname(first_name, last_name) and 
            check_if_valid_email(email) and 
            check_if_valid_number(number) and 
            check_if_valid_password(password)):
            print("Valid user input")
        else:
            print("Invalid user input")
    except Exception as e:
        print(f"Error in main block: {e}")
