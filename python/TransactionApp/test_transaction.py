
import unittest
import transaction_app   

class TestTransactionApp(unittest.TestCase):

    def test_deposit_function_exists(self):
       self.assertTrue(callable(transaction_app.deposit))  
     

    def test_deposit_increases_balance(self):
        actual = transaction_app.deposit(500, 1000)
        expected = 1500

       
        self.assertEqual(actual, expected)
    unittest.main()