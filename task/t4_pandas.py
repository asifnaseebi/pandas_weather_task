import pandas as pd
from datetime import datetime

FILE_PATH = "f2.csv"
data_frame = pd.read_csv(FILE_PATH)

event_thunderstorm_data = data_frame[data_frame[' Events'] == 'Thunderstorm']

event_thunderstorm_days = [datetime.strptime(date, "%Y-%m-%d").strftime("%A")
                           for date in event_thunderstorm_data['PKT']]

print(event_thunderstorm_days)
