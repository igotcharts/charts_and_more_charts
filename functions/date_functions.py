import datetime as dt
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from calendar import isleap
import pandas as pd

def convert_datetime(df):
    datecols = df.dtypes.index[df.dtypes.index.str.contains('DATE')==True].values
    for item in datecols:
        try:
            df[item]= pd.to_datetime(df[item])
        except:
            df[item]=df[item]
