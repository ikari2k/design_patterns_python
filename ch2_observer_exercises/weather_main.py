from ch2_observer_exercises.current_conditions_panel import CurrentConditions
from ch2_observer_exercises.forecast_panel import ForecastPanel
from ch2_observer_exercises.stats_panel import StatsPanel
from ch2_observer_exercises.weather_data import WeatherData

wd: WeatherData = WeatherData()
cd_panel: CurrentConditions = CurrentConditions(wd)
stat_panel:StatsPanel = StatsPanel(wd)
forecast_panel:ForecastPanel = ForecastPanel(wd)


wd.set_measurements(temperature=25, humidity=65, pressure=20)
print('-----------------')
wd.set_measurements(temperature=45, humidity=70, pressure=30)
print('-----------------')
wd.set_measurements(temperature=67, humidity=75, pressure=50)
print('-----------------')
wd.set_measurements(temperature=10, humidity=75, pressure=70)