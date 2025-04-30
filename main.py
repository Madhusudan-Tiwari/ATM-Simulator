UserData={}
def MainMenu():
    print("Welcome to ATM.")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    a=int(input("What would you like to do today."))
    if(a==1):
        Register()
    elif(a==2):
        Login()
    elif(a==3):
        return

def Register():
    while(True):
        NewUser=input("Please enter the account number:")
        if(NewUser in UserData):
            print("User already exists please enter another account number")
        else:
            break
    
    while(True):
        try:
            pin=int(input("Please set a 4 digit pin:"))
            if(len(str(pin))!=4):
                print("The pin must be 4 digit")
            else:
                break
        except ValueError:
            print("Please enter a valid 4 digit pin")
    
    while True:
        try:
            InitialDeposit = float(input("Please set the initial deposit amount: "))
            if InitialDeposit < 0:
                print("Initial deposit must be positive.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    UserData[NewUser]={"pin":pin,"balance":InitialDeposit}
    print("Registration Successful")

    
def Login():
    print("Login to your account")
    Account=input("Enter your account number")
    if(Account not in UserData):
        print("Account not found. Please register first")
        return
    
    while True:
        try:
            Pin=int(input("Please enter your pin"))
            if Pin==UserData[Account]["pin"]:
                print("Login Successful")
                AccountMenu()
                break
            else:
                print("Incorrect pin try again.")
        except ValueError:
            print("Invalid Pin try again")

def AccountMenu():
    pass

MainMenu()