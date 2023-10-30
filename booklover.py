import unittest
import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        """
        Purpose: Initialize class BookLover with name of person, email and favorite genre of books. 
                 num_books is a list that keeps track of the number of books the person has read.
                 book_list is a DataFrame with book_name and book_rating.
        """
        
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        if book_list is None:
            book_list = pd.DataFrame({'book_name': [], 'book_rating': []})
        self.book_list = book_list

    def add_book(self, book_name, rating):
        """
        Purpose: This function takes a book name (string) and rating (integer from 0 to 5) 
                 It tries to add the book to book_list. See hint below on how to pass a new book to the dataframe.
        """
        
        if not self.has_read(book_name):
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print(f" book already read")

    def has_read(self, book_name):
        """
        Purpose: This function takes book_name (string) as input and determines if the person has read the book.
                 The method should return True if the person has read the book, False otherwise.
        """
        
        return book_name in self.book_list['book_name'].tolist()

    def num_books_read(self):
        """
        Purpose: This function takes no parameters and just returns the total number of books the person has read.
        """
        
        return self.num_books

    def fav_books(self):
        """
        Purpose: This function takes no parameters and returns the filtered dataframe of the person’s most favorite books.
                Books in this list should have a rating > 3.
        """
        
        return self.book_list[self.book_list['book_rating'] > 3]

if __name__ == '__main__':

    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)

