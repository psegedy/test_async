import tornado.web
from tornado.ioloop import IOLoop


class MainHandler(tornado.web.RequestHandler):
    """Main handler of Tornado application."""
    def get(self):
        """Handle get request."""
        self.write("Hello, world")


# application with endpoint "/" and handler MainHandler
application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":  # pragma: no cover
    server = tornado.httpserver.HTTPServer(application)
    server.listen(8080)
    IOLoop.instance().start()
