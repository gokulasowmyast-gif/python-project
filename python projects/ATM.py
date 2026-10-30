balance=10000
def show_menu():
    print("\n ATM menu ")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def check_balance():
    print(f"\n>> available balance:{balance}")

def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit:"))
        if amount <= 0:
            print("Error: Amount must be greater than 0")
        else:
            balance += amount
            print(f"Success: {amount} deposited.")
            check_balance()
    except ValueError:
        print("Error: Please enter a valid number")

def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Error: Amount must be greater than 0")
        elif amount > balance:
            print(f"Error: Insufficient funds! Your balance is {balance}")
        else:
            balance -= amount
            print(f"Success: {amount} withdrawn.")
            check_balance()
    except ValueError:
        print("Error: Please enter a valid number")

while True:
    
    show_menu()
    
    choice = input("Select an option (1-4): ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit() 
    elif choice == '3':
        withdraw() 
    elif choice == '4':
        print("\nThank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option! Please choose 1 to 4.")
