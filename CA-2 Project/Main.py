from FileHandling import LoadData
from UserInput import UserRegistration, UserLogin, UserForgotPassword
from ApiModule import FetchNews

def ExitProgram():
    print("Exiting the program. Goodbye!")
    exit()

def main():
    users = LoadData()
    
    while True:
        print("\n--- Login and Signup Page ---")
        print("1. Registration")
        print("2. Login")
        print("3. Forgot password")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                UserRegistration(users)
            case '2':
                country = UserLogin(users)
                if country:
                    FetchNews(country)
            case '3':
                UserForgotPassword(users)
            case '4':
                ExitProgram()
            case _:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
