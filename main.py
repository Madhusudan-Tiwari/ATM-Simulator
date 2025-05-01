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
        print(UserData)
        return

    while True:
        try:
            Pin=int(input("Please enter your pin"))
            if Pin==UserData[Account]["pin"]:
                print("Login Successful")
                AccountMenu(Account)
                break
            else:
                print("Incorrect pin try again.")
        except ValueError:
            print("Invalid Pin try again")

def AccountMenu(Account):
    while True:
        print("Welcome dear customer please proceed with further requests")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Logout")

        try:
            c = int(input())
            if c==1:
                CheckBalance(Account)
            elif c==2:
                WithdrawMoney(Account)
            elif c==3:
                DepositMoney(Account)
            elif c==4:
                return
        except ValueError:
            print("Please enter a valid choice")

def CheckBalance(Account):
    print(UserData[Account]["balance"])

def WithdrawMoney(Account):
    while True:
        try:
            Amount=int(input("Please enter the amount you want to withdraw"))
            if Amount<0:
                print("Please enter a positive amount")
            elif Amount>UserData[Account]["balance"]:
                print("You only have ",UserData[Account]["balance"], "in your account. Please enter within your limits.")
            else:
                UserData[Account]["balance"]-=Amount
                print("Amount withdrawn successfully")
                print("You now have ",UserData[Account]["balance"], "left in your account.")
        
        except ValueError:
            print("Please enter a valid amount")

def DepositMoney(Account):
    while True:
        try:
            Deposit=int(input("Please enter the amount of money you want to add"))
            if Deposit<=0:
                print("Invalid amount unable to deposit")
            else:
                UserData[Account]["balance"]+=Deposit
        except ValueError:
            print("Please enter a valid amount")


MainMenu()