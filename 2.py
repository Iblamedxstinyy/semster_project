class Book():
    def __init__(self, title,author, year, isAvailable):
        self.title = title
        self.author = author
        self.year = year
        self.isAvailable = isAvailable

    def showInfo(self):
        print(f'имя : {self.title},автор : {self.author},год : {self.year},доступна : {self.isAvailable}')

    def borrowBook(self):
        print(f'вы взяли книгу {self.title}')
        self.isAvailable = False

    def returnBook(self):
        print(f'вы вернули книгу {self.title}')
        self.isAvailable = True

    def getAvailability(self):
        print(f'книга доступна : {self.isAvailable}')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'книга добавлина: {book.title}')

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("книгу видалено")
                return

        print("книгу не знайдено")

    def show_all_books(self):
        for book in self.books:
            book.showInfo()

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def show_info(self):
        pass

class Reader(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.borrowed_books = []

    def borrowBook(self, book):
        if book.isAvailable:
            book.isAvailable = False
            self.borrowed_books.append(book)
            print(f'вы взяли книгу {book.title}')
            return True
        else:
            print('книга недоступна')
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.returnBook()
            self.borrowed_books.remove(book)
            print(self.name, "Returned Book", book.title)

    def show_borrowed_books(self):
        if not self.borrowed_books:
            print('нет взятых книг')
        else:
            for book in self.borrowed_books:
                print(book.title)

    def show_info(self):
        print(f'имя : {self.name},год : {self.age}')
class Librarian(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def add_book_to_library(self, library, book):
        library.add_book(book)

    def show_info(self):
        print(f'имя : {self.name},год : {self.age}')

class Admin(Person):

    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, title):
        library.remove_book(title)

    def show_info(self):
        print(self.name, self.age)


library = Library()
librarian = Librarian("Олена", 950)

book1 = Book('Кобзар','Тарас Шевченко', 1840, True)
book2 = Book('Захар Беркут','Іван Франко', 1883, True)

librarian.add_book_to_library(library, book1)
librarian.add_book_to_library(library, book2)

reader = Reader('kolay', 20)

reader.borrowBook(book1)

reader.show_borrowed_books()

reader.borrowBook(book1)

reader.return_book(book1)

while True:
    print('1: все книги')
    print('2: взять книгу')
    print('3: вернуть книгу')
    print('4: поиск по названию')
    print('5: выход')

    q = int(input('ваш выбор'))

    if q == 1:
        Library.show_all_books(library)
    elif q == 2:
        q2 = input('какую книгу вы хотите взять 1 Кобзар !! 2 Захар Беркут')
        if q2 == 1:
            reader.borrowBook(book1)
            reader.show_borrowed_books()
        elif q2 == 2:
            reader.borrowBook(book2)
            reader.show_borrowed_books()
        else:
            print()
    elif q == 3:
        q2 = input('какую книгу вы хотите вернуть 1 Кобзар !! 2 Захар Беркут')
        if q2 == 1:
            reader.return_book(book1)
            reader.show_borrowed_books(reader)
        elif q2 == 2:
            reader.return_book(book2)
            reader.show_borrowed_books(reader)
        else:
            print()
    elif q == 4:
        library.find_book_by_title(library)
    elif q == 5:
        break
    else:
        print('не правельный выбор')

