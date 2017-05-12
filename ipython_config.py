c = get_config()
c.InteractiveShellApp.exec_lines = [
    'import numpy as np',
    'import pandas as pd',
    'pd.set_option(\'display.max_columns\', None)',
    'pd.set_option(\'display.max_rows\', 100)',
    'import matplotlib.pyplot as plt',
    'from pandas import DataFrame, Series',
    'from scipy import stats',
    'from sklearn import linear_model,cross_validation, feature_selection,preprocessing',
    'import statsmodels.formula.api as sm',
    'from statsmodels.tools.eval_measures import mse',
    'from statsmodels.tools.tools import add_constant',
    'from sklearn.metrics import mean_squared_error',
    'import matplotlib as mpl',
    'import matplotlib.dates as mdates',
    'from matplotlib.colors import LinearSegmentedColormap',
    'from matplotlib.lines import Line2D',
    'from matplotlib.font_manager import FontManager',
    'import matplotlib.patches as patches',
    'import matplotlib.colors as col',
    'from matplotlib import cm',
    'import matplotlib.ticker as ticker',
    'from pylab import *',
    'from __future__ import division',
    'from datetime import datetime',
    



]
