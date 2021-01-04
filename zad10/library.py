import json
import sys
from jezyki_biblioteki_analizy_danych.zad10.my_exception import *


class Library:
    def __init__(self):
        self.menu = dict()
        self.books = {1: {'title': 'A Game of Thrones', 'author': 'George R.R. Martin', 'publishment_year': 2011},
                      2: {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'publishment_year': 2005},
                      3: {'title': 'Harry Potter and the Chamber of Secrets', 'author': 'J.K. Rowling',
                          'publishment_year': 2014},
                      4: {'title': 'The Martian', 'author': 'Andy Weir', 'publishment_year': 2014}}

    def books_catalog(self):
        with open('library_books.json', 'w') as json_file:
            json.dump(self.books, json_file, indent=4)


class Reader(Library):
    def __init__(self):
        super().__init__()
        # r1,r2,r3 - identyfikatory ktorymi dany czytelnik sie loguje do systemu
        self.readers = {'r1': 'Harry Potter',
                        'r2': 'Hermiona Granger',
                        'r3': 'Ron Weasley'}

    def reader_menu(self):
        self.menu = {1: 'Search the catalog of books',
                     2: 'Borrow a book'}
        with open('menu_for_reader.json', 'w') as json_file:
            json.dump(self.menu, json_file, indent=4)
        return self.menu

    def readers_catalog(self):
        with open('list_of_readers.json', 'w') as json_file:
            json.dump(self.readers, json_file, indent=4)

    def check_readers_option(self, option):
        if option == "1":
            with open('library_books.json') as json_file:
                self.books = json.load(json_file)
            wanted_book = input('Enter the title or author of the book you are looking for: ')
            books = [self.books[id] for id, value in self.books.items() for key in value if value[key] == wanted_book]
            if not books:
                print("Book is not found")
            else:
                print("Books found in the system: ")
                print(*books, sep='\n')
        elif option == "2":
            with open('library_books.json') as json_file:
                self.books = json.load(json_file)
            n = int(input("Enter the number of books you want to borrow : "))
            titles = [input('Enter the title of the book you want to borrow: ') for i in range(0, n)]
            book = [(id, self.books[id]) for id, value in self.books.items() for key in value if value[key] in titles]
            bookTitles = [b[1]['title'] for b in book]
            for title in titles:
                if title not in bookTitles:
                    print(f"Book \"{title}\" is not found")
            if book:
                print("Borrowed books: ")
                print(*book, sep='\n')

                keys = [tuples[0] for tuples in book]
                values = [tuples[1] for tuples in book]
                borrowedBook = dict(zip(keys, values))
                with open('borrowed_books.json', 'w') as json_file:
                    json.dump(borrowedBook, json_file, indent=4)
                for tuples in book:
                    del self.books[tuples[0]]
            with open('library_books.json', 'w') as json_file:
                json.dump(self.books, json_file, indent=4)
        elif option == 'exit':
            sys.exit('Thank you for using the system!')
        else:
            raise OptionNotFoundError("The specified option does not exist!")


class Worker(Library):
    def __init__(self):
        super().__init__()
        # w1, w2 itd - to identyfikator ktorym pracownik sie loguje do systemu
        self.workers = {'w1': 'Minerwa McGonagall',
                        'w2': 'Severus Snape',
                        'w3': 'Albus Dumbledore'}

    def worker_menu(self):
        self.menu = {1: 'Accept the return of the books',
                     2: 'Add a book',
                     3: 'Delete a book',
                     4: 'Add a reader'}
        with open('menu_for_worker.json', 'w') as json_file:
            json.dump(self.menu, json_file, indent=4)
        return self.menu

    def workers_catalog(self):
        with open('list_of_workers.json', 'w') as json_file:
            json.dump(self.workers, json_file, indent=4)

    def books_output(self):
        for id, value in self.books.items():
            print(f"{id}. {self.books[id]['title']}, {self.books[id]['author']}, {self.books[id]['publishment_year']}")

    def check_workers_option(self, option):
        if option == "1":
            with open('library_books.json') as json_file:
                self.books = json.load(json_file)
            print('Do you want to accept books return? (y / n)')
            decision = input()
            keys = []
            if decision == 'y':
                with open('borrowed_books.json') as json_file:
                    borrowBook = json.load(json_file)
                for key, value in borrowBook.items():
                    self.books[key] = value
                    keys.append(key)
                for k in keys:
                    del borrowBook[k]
                with open('borrowed_books.json', 'w') as json_file:
                    json.dump(borrowBook, json_file, indent=4, sort_keys=True)
                print('The return of the books has been accepted')
            elif decision == 'n':
                print('The return of the books has not been accepted')
            else:
                raise OptionNotFoundError("The specified option does not exist!")
            with open('library_books.json', 'w') as json_file:
                json.dump(self.books, json_file, indent=4, sort_keys=True)

        elif option == "2":
            with open('library_books.json') as json_file:
                self.books = json.load(json_file)
            title = input('Enter the title: ')
            author = input('Enter the author: ')
            year = input('Enter the publishment year: ')
            if type(year) != int or int(year) > 2020:
                raise PublishmentYearError("The specified publishment year is incorrect!")

            self.books[str(len(list(self.books.keys())) + 1)] = {"title": title, "author": author,
                                                                 "publishment_year": year}
            with open('library_books.json', 'w') as json_file:
                json.dump(self.books, json_file, indent=4, sort_keys=True)
            print('The books has been updated:')
            self.books_output()
        elif option == "3":
            with open('library_books.json') as json_file:
                self.books = json.load(json_file)
            key = input('Enter the ID of the book you want to delete: ')
            del self.books[key]
            with open('library_books.json', 'w') as json_file:
                json.dump(self.books, json_file, indent=4, sort_keys=True)
            print('The books has been updated:')
            self.books_output()
        elif option == "4":
            r = Reader()
            with open('list_of_readers.json') as json_file:
                r.readers = json.load(json_file)
            name = input('Enter the new reader: ')
            r.readers[f"r{len(list(r.readers.keys())) + 1}"] = name
            with open('list_of_readers.json', 'w') as json_file:
                json.dump(r.readers, json_file, indent=4, sort_keys=True)
            print('The catalog of readers has been updated:')
            for key, value in r.readers.items():
                print(f"{key}. {value}")
        elif option == 'exit':
            sys.exit('Thank you for using the system!')
        else:
            raise OptionNotFoundError("The specified option does not exist!")


def main():
    w = Worker()
    r = Reader()
    workersID = list(w.workers.keys())
    readersID = list(r.readers.keys())
    print('Welcome to the library system, please log in using your ID:')
    try:
        id = input()
        if id in readersID:
            print(f'Hello {r.readers[id]}, here is your available options:')
            for key, value in r.reader_menu().items():
                print(f"{key}. {value}")
            while True:
                try:
                    r.check_readers_option(option=input('Please select one option: '))
                except (OptionNotFoundError, PublishmentYearError) as e:
                    print(e)
        elif id in workersID:
            print(f'Hello {w.workers[id]}, here is your available options:')
            for key, value in w.worker_menu().items():
                print(f"{key}. {value}")
            while True:
                try:
                    w.check_workers_option(option=input('Please select one option: '))
                except (OptionNotFoundError, PublishmentYearError) as e:
                    print(e)
        else:
            raise IDNotFoundError("There is no user with the given ID!")
    except IDNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()
