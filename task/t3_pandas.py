import pandas as pd
from constants import FILE_PATH_F2, EVENTS_COL

data_frame = pd.read_csv(FILE_PATH_F2)
dates_events = data_frame[data_frame[EVENTS_COL].isin(['Snow', 'Rain', 'Rain-Snow'])]['PKT'].tolist()

print(dates_events)
