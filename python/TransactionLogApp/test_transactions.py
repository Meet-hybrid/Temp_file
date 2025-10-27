import unittest
from transactions import deposit, #withdraw, #show_transactions

class TransactionLogApp(unittest.TestCase):

	def test_transaction_functions(self):
    		balance = 0
    		transactions = []

   
    		
    		balance = deposit(1000, balance, transactions)
    		assert balance == 1000

    		
    		#balance = withdraw(400, balance, transactions)
    		#assert balance == 600
    		

    		
    		#balance = withdraw(1000, balance, transactions)
    		#assert balance == 600 
    		

    
    		#print("\n Testing Show Transactions...")
    		#show_transactions(transactions)

    		


