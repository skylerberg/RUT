class Observable(object):

    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.notify(self)
