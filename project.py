import os
import pandas as pd
import datetime
from itertools import groupby

# os.chdir('D:')
# os.chdir('music')

print(os.getcwd())
with open('MusicData.csv') as my_data:
    df = pd.read_csv(my_data, index_col=5)

start_date = '1990-01-01'
end_date = '2000-01-01'

mask = ((df['WeekID'] > start_date) & (df['WeekID'] <= end_date) ) & (df['Week Position'] < 11)

ninties = df.loc[mask]
