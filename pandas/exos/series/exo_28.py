import numpy as np
import pandas as pd

ser = pd.Series(['01 Jan 2015', '10-02-2016', '20180307',
'2014/05/06', '2016-04-12', '2019-04-06T11:20'])

date_ser = pd.to_datetime(ser)
days_of_month = date_ser.dt.day.tolist()
days_of_year = date_ser.dt.day_of_year.tolist()
days_of_week = date_ser.dt.day_of_week.tolist()
week_number = date_ser.dt.isocalendar().week.tolist()
print(f"Jours du mois : \n {days_of_month}")
print(f"Jours de la semaine : \n {days_of_week}")
print(f"Jours de l'année : \n {days_of_year}")
print(f"Semaines de l'année : \n {week_number}")