from ch2_observer_exercises.observer_interface import Observer
from ch2_observer_exercises.subject_interface import Subject


class WeatherData(Subject):

    def __init__(self):
        self.observers: list[Observer] = []
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.pressure: float = 0.0

    def add_observer(self, observer: Observer):
        if observer not in self.observers:
            self.observers.append(observer)
        print(f'Observer {observer} added to the list of observers')

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()
