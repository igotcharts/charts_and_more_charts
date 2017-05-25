import numpy as np
import pandas as pd
import math
def roundup(x):
       return int(math.ceil(x / 10.0)) * 10

def percent_convert(df,column):
    return '%.1f'%df[column]+'%'
