import unittest
import hybrids_book 

class TestHybridsBook(unittest.TestCase):

    def setUp(self):
        self.books = ["The Hobbit", "The Mystery in Semicolon", "The Brave Hybrid"]

    def test_add_book(self):
        result = hybrids_book.add_book(self.books, "John Wick")
        self.assertEqual(result, "Book added successfully!")
        self.assertIn("John Wick", self.books)

    def test_remove_book(self):
        result = hybrids_book.remove_book(self.books, "The Hobbit")
        self.assertEqual(result, "Book removed successfully!")
        self.assertNotIn("The Hobbit", self.books)

    def test_update_book(self):
        result = hybrids_book.update_book(self.books, "The Brave Hybrid", "Brave Kingdom of Hybrid")
        self.assertEqual(result, "Book updated successfully!")
        self.assertIn("Brave Kingdom of Hybrid", self.books)

    def test_suggest_book(self):
        result = hybrids_book.suggest_book(self.books)
        self.assertTrue(result.startswith("Book Title:"))

    def test_show_books(self):
        result = hybrids_book.show_books(self.books)
        self.assertIn("The Hobbit", result)

