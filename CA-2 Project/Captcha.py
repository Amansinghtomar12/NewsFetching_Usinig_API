import random

def CaptchaVerification():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    print(f"Add the numbers: {num1} + {num2} = ?")
    user_answer = input("Enter the result: ")
    return user_answer == str(num1 + num2)
