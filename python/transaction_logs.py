def get_new_balance(amount):

	new_balance = 0
	new_balance + amount

	return new_balance

def get_balance_after_withdrawal(withdraw):

	withdraw_balance = 0
	withdraw_new_balance = new_balance_withdraw
	
	return withdraw_balance

print("""
welcome to the Transaction Log App

1 -> Deposit
2 -> Withdraw
3 -> Show Transactions
4 -> Exit

""")

for i in range(10):
	options = input("Pick a number from the list of above (1-4): ")

	if options == "1":
	   amount = float(input("Enter deposit amount: "))
	   balance += amount
print("Deposited:", amount, " | New balance:", balance)


