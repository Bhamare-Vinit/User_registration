import re
import logging

# Configure the logger
logging.basicConfig(filename='user.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_if_valid_firstname_lastname(first_name, last_name):
    try:
        if re.search("[A-Z][a-z]{2,}$", first_name) and re.search("[A-Z][a-z]{2,}$", last_name):
            return True
        else:
            logger.error(f"Error validating first name and last name: {e}")
            return False
    except Exception as e:
        logger.error(f"Error validating first name and last name: {e}")
        return False

def check_if_valid_email(email):
    try:
        if re.search(r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$", email):
            return True
        else:
            logger.error(f"Error validating email: {e}")
            return False
    except Exception as e:
        logger.error(f"Error validating email: {e}")
        return False

def check_if_valid_number(number):
    try:
        if re.search(r"^\d{2}\s\d{10}$", number):
            return True
        else:
            logger.error(f"Error validating number: {e}")
            return False
    except Exception as e:
        logger.error(f"Error validating number: {e}")
        return False

def check_if_valid_password(password):
    try:
        pattern = r"^(?=.*[!@#$%^&*()_+{}|:<>?])(?!.*[!@#$%^&*()_+{}|:<>?].*[!@#$%^&*()_+{}|:<>?]).*$"
        if len(password) >= 8:
            if re.search(r"[A-Z]", password) and re.search(r"\d", password) and re.search(r"[a-z]", password) and re.search(pattern, password):
                return True
            else:
                logger.warning("Bad password: Missing required characters")
                return False
        else:
            logger.warning("Bad password: Too short")
            return False
    except Exception as e:
        logger.error(f"Error validating password: {e}")
        return False

if __name__ == "__main__":
    try:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")

        if (check_if_valid_firstname_lastname(first_name, last_name)):
            logger.info(f"Valid user firstname and lastname: {first_name} {last_name}")
            email = input("Enter your email: ")
            if (check_if_valid_email(email)): 
                logger.info(f"Valid user Email: {email}")
                number = input("Enter your mobile number with country code: ")
                if (check_if_valid_number(number)):
                    logger.info(f"Valid user number: {number}")
                    password = input("Enter your password: ")
                    if (check_if_valid_password(password)):
                        logger.info(f"Valid user password: {password}")
                    else:
                        logger.info("Invalid user password")
                else:
                    logger.info("Invalid user number")
            else:
                logger.info("Invalid user Email")
        else:
            logger.info("Invalid user firstname and lastname")
    except Exception as e:
        logger.error(f"Error in main block: {e}")
