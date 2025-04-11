from ch2_observer_exercises.information_panel_interface import InformationPanel
from ch2_observer_exercises.observer_interface import Observer
from ch2_observer_exercises.weather_data import WeatherData


class StatsPanel(InformationPanel, Observer):



    def __init__(self, weather_data: WeatherData):
        self.temperature = 0.0
        self.tempMax: float = 50.0
        self.tempMin: float = 20.0
        self.tempSum: float = 0.0
        self.tempCount: int = 0
        self.weather_data = weather_data
        weather_data.add_observer(self)

    def get_info(self):
        print(f'Avg. temperature / maximum / minimum: {self.tempSum / self.tempCount:.2f} / {self.tempMax} / {self.tempMin}')

    def update(self):
        self.temperature = self.weather_data.temperature
        self.tempSum += self.temperature
        self.tempCount += 1
        if self.weather_data.temperature > self.tempMax:
            self.tempMax = self.weather_data.temperature
        if self.weather_data.temperature < self.tempMin:
            self.tempMin = self.weather_data.temperature
        self.get_info()
