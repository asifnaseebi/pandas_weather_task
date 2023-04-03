import pandas as pd
from constants import FILE_PATH_F1, MAX_TEMP_COL, MIN_TEMP_COL

data_frame = pd.read_csv(FILE_PATH_F1)

max_temperature = data_frame[MAX_TEMP_COL].values
min_temperature = data_frame[MIN_TEMP_COL].values
calculate_temperature_average = (max_temperature - min_temperature) / 2

print(calculate_temperature_average)
