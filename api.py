import tornado.ioloop
import tornado.web
from allHandler import VersionHandler, AddHandler, DelHandler, GetHandler
from book import Book

books = Book()

def create_app():
    return tornado.web.Application([
        (r"/v1", VersionHandler),
        (r"/v1/addbook", AddHandler, dict(books = books)),
        (r"/v1/delbook", DelHandler, dict(books = books)),
        (r"/v1/getbooks", GetHandler, dict(books = books)),
        ])

if __name__ == "__main__":
    app = create_app()
    print("created my webapp and listening on port 8890")
    app.listen(8890)
    tornado.ioloop.IOLoop.current().start()
