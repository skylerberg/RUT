# pylint: disable=too-many-public-methods
import unittest

from rut.observer import Observable, Observer


class ExampleObserver(Observer):

    def __init__(self):
        super(ExampleObserver, self).__init__()
        self.notified_by = None

    def notify(self, observable):
        self.notified_by = observable


class ExampleObservable(Observable):
    pass


class TestObservable(unittest.TestCase):
    """
    This test uses the self-shunt pattern to act as both Observable and
    Observer.
    """

    def setUp(self):
        self.observer = ExampleObserver()
        self.observable = ExampleObservable()

    def test_not_observing(self):
        self.observable.notify_observers()
        self.assertEquals(None, self.observer.notified_by)

    def test_observing(self):
        self.observable.add_observer(self.observer)
        self.observable.notify_observers()
        self.assertEquals(self.observable, self.observer.notified_by)
