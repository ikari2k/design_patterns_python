from ch2_observer_exercises.information_panel_interface import InformationPanel
from ch2_observer_exercises.observer_interface import Observer
from ch2_observer_exercises.weather_data import WeatherData


class ForecastPanel(Observer,InformationPanel):

    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.current_pressure = 30
        self.previous_pressure = 0.0
        weather_data.add_observer(self)

    def get_info(self):
        print(f'Weather forecast:')
        if self.current_pressure > self.previous_pressure:
            print('Improving weather on the way!')
        elif self.current_pressure == self.previous_pressure:
            print('More of the same')
        elif self.current_pressure < self.previous_pressure:
            print('Watch out for cooler, rainy weather')

    def update(self):
        self.previous_pressure = self.current_pressure
        self.previous_pressure = self.weather_data.pressure
        self.get_info()