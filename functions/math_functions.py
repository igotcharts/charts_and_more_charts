import numpy as np
import pandas as pd
import math
def roundup(x):
       return int(math.ceil(x / 10.0)) * 10

def percent_convert(df,column):
    return '%.1f'%df[column]+'%'

def myround(x, base=5):
    return int(base * round(float(x)/base))


def percent_convert(x,percent_format):
    """
    Converts a series to percent text format

    Parameters
    ------------
    "pecent_format": boolean. If series values are already in percent format, set as True. Otherwise set as false.

    """
    if percent_format == True:
        return '%.1f'%(x*100)+'%'
    else:
        return '%.1f'%x+'%'
