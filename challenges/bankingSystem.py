#a banking system that allows users to create account, deposit,withdraw & transfer money and also shows transaction history

#to deposit balance
def depositBalance():
    amount= float(input("Enter the amount of money you want to deposit:"))    
    if amount<=0:
        print("INVALID AMOUNT!!! \n Please enter amount greater than 0")
        return 0
    else: return amount
#to check balance


def checkBalance(balance):
    print(f"your balance is Rs.{balance:.2f}")

#to deposit balance
def depositBalance():
    amount= float(input("Enter the amount of money you want to deposit:"))    
    if amount<=0:
        print("INVALID AMOUNT!!! \n Please enter amount greater than 0")
        return 0
    else: return amount

#to withdraw balance    
def withdrawBalance(balance):
    amount= float(input("Enter the amount of money you want to deposit:"))    
    if amount<=0:
        print("INVALID AMOUNT!!! \n Please enter amount greater than 0")
        return 0
    elif amount>balance:
        print("INSUFFICIENT AMOUNT \n Please enter valid amount")
        return 0
    else:
        return amount
    
#to transfer balance  
def transferBalance(balance):
    amount= float(input("Enter the amount of money you want to transfer:"))    
    if amount<=0:
        print("INVALID AMOUNT!!! \n Please enter amount greater than 0")
        return 0
    elif amount>balance:
        print("INSUFFICIENT AMOUNT \n Please enter valid amount")
        return 0
    else:
        return amount  
    
#to show transaction history
def transactionHistory(transactions):
    print("Transaction History")
    for transaction in transactions:
        print(transaction)

def main():
    accounts={}    
    currentAccount=""
    transactions=[]
    isss= True
    while isss :
        print("\n")
        print("Welcome to Dreams Bank🤗")
        print("🤍🤍🤍🤍🤍 \n")
        print("Please select any one:")
        print("1.To create account")
        print("2.To select account")
        print("3.To show balance")
        print("4.To deposit balance")
        print("5.To withdraw balance")
        print("6.To transfer balance")
        print("7.Show transaction history")
        print("8.Exit")

        choice = input("Choose between 1-8 :")

        if choice=="1":
            accountName= input("Enter your account name:")
            if accountName in accounts: print("Your account already exists. Please proceed further.")
            else:
                accounts[accountName]=0
                print(f"Your account {accountName} is created.")
        elif choice=='2':
             accountName= input("Enter your account name:")
             if accountName in accounts: 
                 currentAccount= accountName
                 print(f"Account {currentAccount} has been selected")
             else:
                print(f"Account {currentAccount} does not exist. Please create an account first. ")
        elif choice=='3' :
            if currentAccount in accounts:
                checkBalance(accounts[currentAccount])
            else: print("NO ACCOUNTS SELECTED!!")    
        elif choice == '4':
            if currentAccount:
                amount = depositBalance()
                accounts[currentAccount] += amount
                transactions.append(f"Deposited Rs.{amount:.2f} to Account number: {currentAccount}")
            else:
                print("NO ACCOUNTS SELECTED!")

        elif choice == '5':
            if currentAccount:
                amount = withdrawBalance(accounts[currentAccount])
                accounts[currentAccount] -= amount
                transactions.append(f"Withdrew Rs.{amount:.2f} from Account number: {currentAccount}")
            else:
                print("NO ACCOUNTS SELECTED!")

        elif choice == '6':
            if currentAccount:
                transferAccount = input("Enter transfer account name: ")
                if transferAccount in accounts:
                    amount = transferBalance(accounts[currentAccount])
                    if amount > 0:
                        accounts[currentAccount] =accounts[currentAccount]- amount
                        accounts[transferAccount] =accounts[transferAccount] + amount
                        transactions.append(f"Transferred Rs.{amount:.2f} from Account number: {currentAccount} to Account number: {transferAccount}")
                else:
                    print("Transfer account does not exist.")
            else:
                print("NO ACCOUNTS SELECTED!")

        elif choice == '7':
            transactionHistory(transactions)

        elif choice == '8':
             isss= False
        else:
    
            print("That is not a valid choice")
    

    print("Thank you for visiting. Have a nice day🤍!")

if __name__ == '__main__':
    main()