import tornado.web
import book
import json

class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("sample microservice v1")

class MyWebHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
    def get(self):
        pass

class AddHandler(MyWebHandler):
    def get(self):
        title = self.get_argument('title')
        author = self.get_argument('author')
        result = self.books.add_book(title, author)
        self.write(result)

class DelHandler(MyWebHandler):
    def get(self):
        title = self.get_argument('title')
        result = self.books.del_book(title)
        if result:
            self.write("Deleted book title: {0} successfully".format(title))
            self.set_status(200)
        else:
            self.write("Book '{0}' not found".format(title))
            self.set_status(404)

class GetHandler(MyWebHandler):
    def get(self):
        #self.write(self.books.json_list())
        self.render("bookList.html", title="Books List", results=self.books.get_all_books())
        self.set_status(200)

