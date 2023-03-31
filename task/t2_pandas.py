import pandas as pd

FILE_PATH = "f1.csv"
data_frame = pd.read_csv(FILE_PATH)

MAX_TEMP_COL = 'Max TemperatureC'
MIN_TEMP_COL = 'Min TemperatureC'

max_temperature = data_frame[MAX_TEMP_COL].values
min_temperature = data_frame[MIN_TEMP_COL].values
calculate_temperature_average = (max_temperature - min_temperature) / 2

print(calculate_temperature_average)

