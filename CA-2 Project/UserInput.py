from FileHandling import LoadData, SaveData
from ApiModule import FetchNews
from Captcha import CaptchaVerification
from CodeValidation import ValidateUsername, ValidateEmail, ValidateMobileNumber, ValidatePassword, HashPassword

MaxLoginAttempts = 5

  # USER REGISTRATION FUNCTION
  
def UserRegistration(users):
    print("\n--- User Registration ---")
    
    uName = input("Enter the username: ")
    while not ValidateUsername(uName):
        print("Invalid username! Username must be more than 4 characters!")
        uName = input("Enter the username: ")
    
    eAddress = input("Enter the email address: ")
    while not ValidateEmail(eAddress):
        print("Invalid email format! Please try again.")
        eAddress = input("Enter the email address: ")

    mNumber = input("Enter the mobile number: ")
    while not ValidateMobileNumber(mNumber):
        print("Mobile number must be in correct format! Try again.")
        mNumber = input("Enter the mobile number: ")

    wPass = input("Enter the new password: ")
    while not ValidatePassword(wPass):
        print("Password must be at least 8 characters long and contain at least one special character! Try again.")
        wPass = input("Enter the new password: ")
    while True:
        cPass = input("Confirm the password: ")
        if wPass == cPass:
            break
        else:
            print("Passwords do not match! Try again.")
         
    print("\nChoose a security question:")
    SecurityQuestions = [
        "What is the name of your pet?",
        "What is your favorite sport?",
        "What is your favorite color?",
        "What is your lucky number?"
    ]
    
    for index, question in enumerate(SecurityQuestions, 1): 
        print(f"{index}. {question}")
        
    try:
        QuestionChoice = int(input("Enter the number of the chosen question: "))
        if (QuestionChoice >= 1 and QuestionChoice <= len(SecurityQuestions)):
            SecurityQuestion = SecurityQuestions[QuestionChoice - 1]
        else:
            print("Invalid choice. Please try again.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    SecurityAnswer = input("Answer the security question: ")
    
    if not CaptchaVerification():
        print("CAPTCHA verification failed! Try again.")
        return

    HashedPassword = HashPassword(wPass)
    HashedSecurityAnswer = HashPassword(SecurityAnswer.lower())

    users.append({
        'Username': uName,
        'EmailAddress': eAddress,
        'PhoneNumber': mNumber,
        'SecurityQuestion': SecurityQuestion, 
        'SecurityAnswer': HashedSecurityAnswer,
        'Wpassword': HashedPassword
    })
    SaveData(users)
    print("Registration successful!")
    
    
  # USER LOGIN FUNCTION

def UserLogin(users):
    users = LoadData()
    print("\n--- User Login ---")
    eAddress = input("Enter your email address: ")

    if not ValidateEmail(eAddress):
        print("Invalid email format! Please try again.")
        return

    user_found = False
    for user in users:
        if user['EmailAddress'] == eAddress:
            user_found = True
            break

    if not user_found:
        print("Email does not exist! Please try again.")
        return

    login_attempts = 0

    while (login_attempts < MaxLoginAttempts):
        wPass = input("Enter your password: ")
        hashed_password = HashPassword(wPass)

        for user in users:
            if user['EmailAddress'] == eAddress and user['Wpassword'] == hashed_password:
                
                if not CaptchaVerification():
                    print("CAPTCHA verification failed! Try again.")
                    return

                print("Login successful!")
                print(f"Welcome, {user['Username']}!")
                
                while True:
                    print("\nOptions:")
                    print("1. Get news for a country")
                    print("2. Logout")
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        country = input("Enter your country for news: ")
                        FetchNews(country)
                    elif choice == '2':
                        print("Logging out...")
                        return
                    else:
                        print("Invalid choice. Please try again.")

        print(f"Invalid email or password! You have {MaxLoginAttempts - login_attempts - 1} attempts left.")
        login_attempts += 1

    print("Too many failed attempts! You have been logged out.")
    return None

 
  # USER FORGOT PASSWORD FUNCTION

def UserForgotPassword(users):
    users = LoadData()
    print("\n--- Forgot Password ---")
    eAddress = input("Enter your email address: ")

    if not ValidateEmail(eAddress):
        print("Invalid email format! Please try again.")
        return

    for user in users:
        if user['EmailAddress'] == eAddress:
            print(f"User found: {user['Username']}")
            print(f"Security Check: {user['SecurityQuestion']}")
            security_answer = input("Answer the security question: ").lower()

            hashed_security_answer = HashPassword(security_answer)

            if hashed_security_answer == user['SecurityAnswer']:
                new_pass = input("Enter your new password: ")

                while not ValidatePassword(new_pass):
                    print("Password must be at least 8 characters long and contain at least one special character! Try again.")
                    new_pass = input("Enter your new password: ")

                confirm_pass = input("Confirm your new password: ")

                if new_pass != confirm_pass:
                    print("Passwords do not match! Try again.")
                    return

                if not CaptchaVerification():
                    print("CAPTCHA verification failed! Try again.")
                    return

                user['Wpassword'] = HashPassword(new_pass)
                SaveData(users)
                print("Password reset successful!")
                return
            else:
                print("Security answer is incorrect.")
                return

    print("No account found with this email address!")
