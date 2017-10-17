import argparse
import os
import json
import tornado.web

log_dirs = None


class MainPageHandler(tornado.web.RequestHandler):
    def get(self):
        global log_dirs
        self.write(
"<!DOCTYPE html>\
<html lang=\"en\">\
<head>\
    <meta charset=\"UTF-8\">\
    <title>{{dir}}</title>\
</head>\
<body><p>Select the log you would like to monitor</p>" +
            " ".join(["<p><a href=\"dir/" + log_dirname + "\">" + log_dirname + "</a></p>" for log_dirname in log_dirs]) +
"</body>\
</html>"
        )


class DirHanlder(tornado.web.RequestHandler):
    def get(self, log_dirname):
        self.render("index.html", dir=log_dirname)

    def post(self, log_dirname):
        if log_dirname.endswite('/'):
			log_dirname = log_dirname[:-1]
        self.redirect("/plot/" + log_dirname + "/" + self.get_argument('plot_name'))


class PlotHandler(tornado.web.RequestHandler):
    def get(self, mixed_path):
        try:
            log_dirname, mixed_path = mixed_path.split('/')
            plot_paths = mixed_path.split('+')
            data = []
            for plot_path in plot_paths:
                with open(os.path.join(log_dirname, plot_path + '.json'), 'r') as f:
                    data.append(json.load(f))

            self.render("plot.html", data=json.dumps(data))

        except IOError:
            self.write("File Not Found!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Training Monitor")
    parser.add_argument("-p", "--port", type=int, default=1111)
    parser.add_argument("-d", "--dir", type=str, action='append', default=[])
    args = parser.parse_args()

    log_dirs = args.dir
    app = tornado.web.Application([
        (r"/", MainPageHandler),
        (r"/dir/(.*)", DirHanlder),
        (r"/plot/(.*)", PlotHandler),
    ],
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        template_path=os.path.join(os.path.dirname(__file__), "template"),
    )
    app.listen(args.port)
    tornado.ioloop.IOLoop.current().start()
