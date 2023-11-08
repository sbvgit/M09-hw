import unittest
from booklover.booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        """
        Purpose: add a book and test if it is in `book_list`
        """
        
        test_object_1 = BookLover("Swaroop", "swaroop@hotmail.com", "History")
        test_object_1.add_book("JFK", 4)
        self.assertTrue(test_object_1.has_read("JFK"))

    def test_2_add_book(self):
        """
        Purpose: add the same book twice. Test if it's in `book_list` only once
        """
        
        test_object_2 = BookLover("Mike", "mike@hotmail.com", "Science")
        test_object_2.add_book("Biology 101", 4)
        test_object_2.add_book("Biology 101", 4)
        book_count = test_object_2.book_list['book_name'].value_counts().get("Biology 101", 1)
        self.assertEqual(test_object_2.num_books_read(), 1)

    def test_3_has_read(self):
        """
        Purpose: pass a book in the list and test if the answer is `True'
        """
        
        test_object_3 = BookLover("June", "june@hotmail.com", "CliFi")
        test_object_3.add_book("SolarWinds", 4)
        self.assertTrue(test_object_3.has_read("SolarWinds"))

    def test_4_has_read(self):
        """
        Purpose: pass a book NOT in the list and use `assert False` to test if the answer is `True`
        """
        
        test_object_4 = BookLover("Jason", "jason@hotmail.com", "Military")
        self.assertFalse(test_object_4.has_read("Madeup"))

    def test_5_num_books_read(self):
        """
        Purpose: add some books to the list, and test num_books matches expected
        """
        
        test_object_5 = BookLover("Rob", "rob@hotmail.com", "Gardening")
        test_object_5.add_book("Roses", 4)
        test_object_5.add_book("Tulips", 3)
        test_object_5.add_book("Begonias", 5)
        self.assertEqual(test_object_5.num_books_read(), 3)

    def test_6_fav_books(self):
        """
        Purpose:  add some books with ratings to the list and check that the returned books have a rating > 3
        """
        
        test_object_6 = BookLover("Jen", "jen@hotmail.com", "Fashion")
        test_object_6.add_book("Hair", 4)
        test_object_6.add_book("Face", 3)
        test_object_6.add_book("Skin", 5)
        test_object_6.add_book("Design", 2)
        fav_books = test_object_6.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))

if __name__ == '__main__':

    unittest.main(verbosity=3)
