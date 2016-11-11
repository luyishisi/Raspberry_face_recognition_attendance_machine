import tornado.ioloop
import tornado.web
import subprocess
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        subprocess.call(["raspistill", "-w", "200", "-h", "200","-e", "jpg", "-n", "-t", "1", "-o", "/home/pi/images/live.jpg"])
        time.sleep(2)
        self.write('<! DOCTYPE html><head>'+
                '<META HTTP_EQUIV="refresh"' +
                'CONTENT="5"></head><body>' +
                '<img src="/images/live.jpg"></body>')
class ImageHandler(tornado.web.StaticFileHandler):
    def set_extra_headers(self, path):
        self.set_header('Cache-Control',
                'no-store, no-cache,must-revalidate,'+
                ' max-age=0')
application = tornado.web.Application([
    (r"/",MainHandler),
    (r"/images/(.*)", ImageHandler,{"path":"/home/pi/images"})])

if __name__== "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()

