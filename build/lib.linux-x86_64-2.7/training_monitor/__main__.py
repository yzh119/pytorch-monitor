import argparse
import os
import json
import tornado.web

info_dir = None

class MainPageHandler(tornado.web.RequestHandler):
    def get(self):
        global info_dir
        self.render("index.html", dir=info_dir)

    def post(self):
        global plot_path
        self.redirect("/plot/" + self.get_argument('plot_name'))


class PlotHandler(tornado.web.RequestHandler):
    def get(self, mixed_path):
        try:
            plot_paths = mixed_path.split('+')
            data = []
            for plot_path in plot_paths:
                with open(os.path.join(info_dir, plot_path + '.json'), 'r') as f:
                    data.append(json.load(f))
            
            self.render("plot.html", data=json.dumps(data))
        
        except IOError:
            self.write("File Not Found!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Training Monitor")
    parser.add_argument("-p", "--port", type=int, default=1111)
    parser.add_argument("-d", "--dir", type=str, default="C:\\Users\\v-ziye\\Documents\\training_monitor\\try")
    args = parser.parse_args()

    info_dir = args.dir
    app = tornado.web.Application([
        (r"/", MainPageHandler),
        (r"/plot/(.*)", PlotHandler),
    ],
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        template_path=os.path.join(os.path.dirname(__file__), "template"),
    )
    app.listen(args.port)
    tornado.ioloop.IOLoop.current().start()
