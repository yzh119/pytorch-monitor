# Training Monitor
A naive tool to visualize training process with the help of [chart.js](http://www.chartjs.org/).

## Requirements

- Python 2.7
- [Tornado](http://www.tornadoweb.org/en/stable/)
- [Chart.js](http://www.chartjs.org/)

## Usage

For client end use:

    import training_monitor.logger as tmlog

    logger = tmlog.Logger('train_v0.1')
    for epoch in range(n_epochs):
        loss = get_loss()
        acc = get_acc()
        logger.add_scalar('acc', acc, epoch)
        logger.add_scalar('loss', loss, epoch)

For server end use:

    python -m training_monitor -p PORT -d DIR

## Reference

- https://github.com/tornadoweb/tornado/tree/stable/demos/chat
- https://github.com/Determinant/lab_monitor/