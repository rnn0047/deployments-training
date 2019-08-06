import json
class Book:
    def __init__(self):
        self.books = []
        #Intialize a temp list
        self.add_book('Writing 101: My first attempt', 'Ram Nagpure')
        self.add_book('Alpha vs Beta: Why it matters?', 'Ram Nagpure')
        self.add_book('Aliens among us', 'Ram Nagpure')

    def add_book(self, title, author):
        new_book = {}
        new_book["Title"] = title
        new_book["Author"] = author
        self.books.append(new_book)
        return json.dumps(new_book)

    def del_book(self, title):
        found = False
        for idx, book in enumerate(self.books):
            if book["Title"] == title:
                index = idx
                found = True
                print("Deleting Book: {0}".format(self.books[idx]))
                del self.books[idx]
        return found

    def get_all_books(self):
        return self.books

    def json_list(self):
        return json.dumps(self.books)
        #return json.dumps(self.books, indent=4, sort_keys=True)
