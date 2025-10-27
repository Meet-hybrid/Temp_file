def deposit(amount, account_balance, transactions):
    account_balance += amount
    transactions.append(f"Deposited: amount | New Balance: account_balance")
    return account_balance


def withdraw(amount, account_balance, transactions):
    if amount <= account_balance:
        account_balance -= amount
        transactions.append(f"Withdrew: amount | New Balance: account_balance")
    else:
        transactions.append("Withdrawal failed: insufficient funds")
    return account_balance


