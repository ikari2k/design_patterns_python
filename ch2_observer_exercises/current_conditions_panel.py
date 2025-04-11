from ch2_observer_exercises.information_panel_interface import InformationPanel
from ch2_observer_exercises.observer_interface import Observer
from ch2_observer_exercises.weather_data import WeatherData


class CurrentConditions(InformationPanel,Observer):

    def __init__(self, weather_data: WeatherData):
        self.weather_data: WeatherData = weather_data
        self.temperature:float = 0.0
        self.humidity:float = 0.0
        self.pressure:float = 0.0
        weather_data.add_observer(self)

    def get_info(self):
        if self.temperature is not None and self.humidity is not None:
            print(f'Current conditions: {self.temperature} C degrees, {self.humidity}% humidity and {self.pressure}')
        else:
            print("Current conditions: No data available yet.")\

    def update(self):
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.pressure = self.weather_data.pressure
        self.get_info()