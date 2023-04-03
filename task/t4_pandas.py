import pandas as pd
from datetime import datetime
from constants import FILE_PATH_F2, EVENTS_COL

data_frame = pd.read_csv(FILE_PATH_F2)

event_thunderstorm_data = data_frame[data_frame[EVENTS_COL] == 'Thunderstorm']
event_thunderstorm_days = [datetime.strptime(date, "%Y-%m-%d").strftime("%A")
                           for date in event_thunderstorm_data['PKT']]

print(event_thunderstorm_days)
