account=0
pin=0

def setpin(pin):
    while True:
        newpin=int(input("Enter your new pin to set"))
        if newpin>1000 and newpin<9999:
            conpin=int(input("ReEnter your new pin to set"))
            if(newpin==conpin):
                print("PIN set successfuly")
                return newpin
            else:
                print("Try again!")
        else:
            print("Enter only 4 digits")
        
def deposit(account):
    deposit=int(input("Enter the amount to deposit"))
    account=account+deposit
    print("Your deposited amount is ",account)
    return account

def withdraw(account):
    amount=int(input("Enter the amount to withdraw cash"))

    if(amount>account):
        print("Insufficient balance")
    else:
        account=account-amount   
        print("Your withdrawl amount",account)

    return account

def balance(account):
    print("your balance is",account)
    
def changepin(pin):
    oldpin=int(input("Enter the old pin"))
    if(oldpin==pin):
        changepin=int(input("Enter the new pin to change"))
        pin=changepin
        print("Successfully changed",changepin)
    else:
        print("invalid pin")

    return pin
        

pin=setpin(pin)


while(1):
    print("---WELCOME TO ATM Mechaine---")
    card=input("Enter your card\n")
    if(card=="yes"):
        accesspin=int(input("Enter your pin to access"))
        if(accesspin==pin):
            ch=int(input("Enter your account type \n1.Savings\n2.Current")) 
            if(ch==1):
                print("---SERVICE SHOWCASE---")
                choice=int(input("Enter your choice \n1.Cash deposit\n2.Cash Withdraw\n3.balance\n4.Change pin\n5.Exit "))
                match choice:

                    case 1:
                        account=deposit(account)

                    case 2:
                        account=withdraw(account)

                    case 3:
                        account=balance(account)
                    case 4:
                        pin=changepin(pin)
                    case 5:
                        print("Thank You")
                        break

                    case _:
                        print("Invalid choice")
            else:
                print("Wrong account type")

        else:
            print("access denied")
    else:
        print("*******")






