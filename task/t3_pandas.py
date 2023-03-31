import pandas as pd

FILE_PATH = "f2.csv"
data_frame = pd.read_csv(FILE_PATH)

dates_events = data_frame[data_frame[' Events'].isin(['Snow', 'Rain', 'Rain-Snow'])]['PKT'].tolist()

print(dates_events)
