# Training Monitor
A naive tool to visualize training process with the help of [chart.js](http://www.chartjs.org/).

## Features
- [x] Monitor several variables simultaneously is supported now.
  - Just fill in the blank with variable names(seperated by '`+`'): `varname1+varname2+...+varnamek`.
- [x] Monitor several logs is supported now.
## Requirements

- Python 2.7
- [Tornado](http://www.tornadoweb.org/en/stable/)
- [Chart.js](http://www.chartjs.org/)

## Install

```bash
make install
```

## Usage

For client end use:

```python
import training_monitor.logger as tmlog

logger = tmlog.Logger('train_v0.1')
for epoch in range(n_epochs):
    loss = get_loss()
    acc = get_acc()
    logger.add_scalar('acc', acc, epoch)
    logger.add_scalar('loss', loss, epoch)
```

For server end use:

    python -m training_monitor -p PORT -d DIR1 [-d DIR2 ...]

## Reference

- https://github.com/tornadoweb/tornado/tree/stable/demos/chat
- https://github.com/Determinant/lab_monitor/
