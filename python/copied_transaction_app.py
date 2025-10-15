def get_new_balance(amount):

	new_balance = 0
	new_balance + amount

	return new_balance

def get_balance_after_withdrawal(withdraw):

	withdraw_balance = 0
	withdraw_new_balance = new_balance_withdraw
	
	return withdraw_balance

for i in range(10):  
    print("""
    Welcome to the Transaction Log App

    1 -> Deposit
    2 -> Withdraw
    3 -> Show Transactions
    4 -> Exit
    """)

    option = input("Pick a number from the list (1 - 4): ")

    if option == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        transactions.append(f"Deposited: {amount}")
        print(f"Deposited {amount}. New balance: {balance}")

    elif option == "2":
        withdraw = float(input("Enter withdrawal amount: "))
        if withdraw > balance:
            print("Insufficient balance!")
        else:
            balance -= withdraw
            transactions.append(f"Withdrew: {withdraw}")
            print(f"Withdrew {withdraw}. New balance: {balance}")

    elif option == "3":
        print("\n--- Transactions so far ---")
        for t in transactions:
            print(t)
        print("---------------------------")

    elif option == "4":
        print("Thank you for using the Transaction Log App!")
        break  
    else:
        print("Invalid option! Please pick between 1 and 4.")