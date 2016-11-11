import tornado.ioloop
import tornado.web
import subprocess

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<! DOCTYPE html><head>'+
                '<META HTTP_EQUIV="refresh"' +
                'CONTENT="5"></head><body>' +
                '<img src="/images/live.jpg"></body>')
class ImageHandler(tornado.web.StaticFileHandler):
    def set_extra_headers(self, path):
        self.set_header('Cache-Control',
                'no-store, no-cache,must-revalidate, max-age=0')
        
application = tornado.web.Application([
    (r"/",MainHandler),
    (r"/images/(.*)", ImageHandler,{"path":"/home/pi/images"})])

if __name__== "__main__":
    subprocess.Popen(["python","lianxuzhibo.py"])
    application.listen(8899)
    tornado.ioloop.IOLoop.instance().start()


