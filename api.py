import tornado.ioloop
import tornado.web
from allHandler import VersionHandler, AddHandler, DelHandler, GetHandler
from book import Book

class BookApp:
    def __init__(self):
        self.books = Book()
        self.port = 8000

    def run(self):
        ba = self.create_app()
        ba.listen(self.port)
        print("created BookApp and listening on port {}".format(self.port))
        tornado.ioloop.IOLoop.current().start()

    def create_app(self):
        return tornado.web.Application([
            (r"/v1", VersionHandler),
            (r"/v1/addbook", AddHandler, dict(books = self.books)),
            (r"/v1/delbook", DelHandler, dict(books = self.books)),
            (r"/v1/getbooks", GetHandler, dict(books = self.books)),
            ])


#for tornadoweb async web framework; use below format
def main():
    app = BookApp()
    app.run()

if __name__ == "__main__":
    main()

