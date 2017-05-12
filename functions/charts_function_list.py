import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
from matplotlib.font_manager import FontManager
import matplotlib.patches as patches
import matplotlib.colors as mcolor
from matplotlib import cm
import matplotlib.ticker as ticker

def folder_setup():
    current_dir = os.getcwd()
    os.chdir('..')
    base_path = os.getcwd()
    data_folder = (os.path.join(base_path,'data'))
    output_folder = (os.path.join(base_path,'outputs'))
    return base_path, data_folder,output_folder

def numeric_code(df,column,first_number=1):
    d = {x:i for i,x in enumerate(df[column].unique())}
    return df[column].map(d)+first_number

def line_chart(x,y,xlabel=None,ylabel=None,title=None,
               figsize=(11,8),title_font=20,top=.9,labelsize=18,tickmarksize=16,
              source=None,marker=None,markersize=5,
              chart_tag='www.igotcharts.com, 2017',source_y=-.16,chart_tag_y=-.19,
              linewidth=2,linecolor='Black'):

    fig = plt.figure(figsize=figsize)
    fig.suptitle(title,fontsize=title_font)
    ax = fig.add_subplot(111)
    plt.subplots_adjust(top=top)
    plt.plot(x,y,linewidth=linewidth,color=linecolor,
    clip_on=False,marker=marker,markersize=markersize)

    #set the x and y axis limits

    ax.set_xlim(x.min(),x.max())
    ax.set_ylim(y.min(),y.max())

    #set the tick intervals - need to add

    #label axes
    ax.set_xlabel(xlabel,fontsize=labelsize)
    ax.set_ylabel(ylabel,fontsize=labelsize)

    ax.grid(alpha=.4)

    #format tick labels
    ax.tick_params(axis='both', which='major', labelsize=tickmarksize,labelcolor='#737373',pad=10)

    ax.text(0,source_y,source,transform=ax.transAxes,fontsize=14,alpha=.4)

    ax.text(0,chart_tag_y,chart_tag,transform=ax.transAxes,fontsize=14,alpha=.4)

    return fig, ax
