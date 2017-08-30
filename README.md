# Training Monitor
A naive tool to visualize training process with the help of [chart.js](http://www.chartjs.org/).

## Features
Visualize multiple variables at a time is supported now.

Just fill in the blanks with `varname1+varname+...` (split by `+`).

## Requirements

- Python 2.7
- [Tornado](http://www.tornadoweb.org/en/stable/)
- [Chart.js](http://www.chartjs.org/)

## Install

Add this line to your `.bashrc`:

	export PYTHONPATH=[clone path]/training_monitor:$PYTHONPATH

Then run the following command in your terminal:

	source ~/.bashrc


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

    python -m training_monitor -p PORT -d DIR

## Reference

- https://github.com/tornadoweb/tornado/tree/stable/demos/chat
- https://github.com/Determinant/lab_monitor/
