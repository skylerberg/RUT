import abc


class Observable(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.notify(self)

    @staticmethod
    def notify_after(func):
        def new_func(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self.notify_observers()
        return new_func


class Observer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def notify(self, observable):
        pass
