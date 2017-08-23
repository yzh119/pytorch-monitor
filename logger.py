import socket
import json
import os

log_upper_bound = 100000


class Logger(object):
    def __init__(self, path):
        self.path = os.path.join(os.getcwd(), path)
        self.counter = 0
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def add_scalar(self, var_name, val, timestamp):
        self.counter += 1
        assert self.counter < log_upper_bound, "Log Limit Exceeded."
        json_path = os.path.join(self.path, var_name + '.json')
        try:
            with open(json_path) as f:
                upd = json.load(f)
            data = upd['data']
        except FileNotFoundError:
            upd = {'label': var_name}
            data = []

        data.append({'x': timestamp, 'y': val})
        upd.update({'data': data})
        with open(json_path, 'w') as f:
            json.dump(upd, f)

if __name__ == '__main__':
    log = Logger('try')
    log.add_scalar('acc', 50, 1)
    log.add_scalar('acc', 40, 2)
    log.add_scalar('acc', 60, 3)
    log.add_scalar('loss', 5, 1)
    log.add_scalar('loss', 4, 2)
    log.add_scalar('loss', 3, 3)
