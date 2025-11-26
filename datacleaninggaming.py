import pandas as pd
import numpy as np
import matplotlib as plt

#visualization
df = pd.read_csv('gaming-session-retention-trends.csv', sep=';')
df.head()
print('The first 5 rows of the gaming session retention trends data:')
print(df.head(), "\n")

#description of columns in int
df.describe()
print('Description of columns in int:')
print(df.describe(), "\n")

#if there are na values
print("Check if there's still na values")
print(df.isnull().sum(), "\n\n")

#fills missing values
print('Now filling missing values for region... \n\n')
df['region'] = df['region'].fillna("Unknown")

#convert string timestamp into actual pandas timestamp
df['session_start_datetime'] = pd.to_datetime(df['session_start_datetime'], dayfirst=True)
df['session_end_datetime'] = pd.to_datetime(df['session_end_datetime'], dayfirst = True)
print('Convert string timestamp into actual pandas timestamp')
print(df[['session_start_datetime', 'session_end_datetime']], '\n')

#recalculate to fix anomaly values in session duration minutes and change type
df['session_duration_minutes'] = np.ceil((df['session_end_datetime'] - df['session_start_datetime']).dt.total_seconds() / 60).astype(int)
print('Re-calculate to fix anomaly values in session duration minutes column and change its type:')
print(df['session_duration_minutes'], '\n')

# fix retention rate value
df['retention_rate'] = pd.to_numeric(df['retention_rate'], errors='coerce')
df['retention_rate'] = df['retention_rate'] / 10
df['retention_rate'] = df['retention_rate'].round().astype(int)
print(df['retention_rate'])

#order the date by using sort_values
print('Order the date by using sort_values:')
df = df.sort_values('session_start_datetime')
print(df['session_start_datetime'], '\n')

#to csv
df.to_csv('gaming-session-retention-trends-cleaned.csv', index=False)
print('Successfully exported cleaned csv')