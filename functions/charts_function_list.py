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
import string
import random

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

def multi_numeric_index(df):
    numeric_index = []
    for item in df.index.get_level_values(0).unique():
        numeric_index.append(list([i for i,v in enumerate(df.loc[item].values)]))
    single_list_index = [item for sublist in numeric_index for item in sublist]
    df.set_index([df.index,single_list_index],inplace=True)
    return df

class chart_maker(object):

    """
    Class to assist with matplotlib charts
    ------
    Initialize object with:

    title = title for plot
    title_size = title_size for plot
    alpha = transparency for plot
    ------

    """
    def __init__(self,title='Title',title_size=16,alpha=.8):
        self.title = title
        self.title_size = title_size
        self.alpha = alpha

    def initial_fig_axis(self,figsize=(11,8)):
        """
        Sets up the matplotlib figure
        set_equal to fig for use with subsequent functions
        ------

        figsize = size of the figure
        ------
        Returns figure

        """
        fig = plt.figure(figsize=figsize)
        fig.suptitle(self.title,fontsize=self.title_size,alpha=self.alpha)
        return fig

    def axes_set_up(self,fig,rows=1,columns=1,plot_num=1):
        """
        Sets up the matplolibt axes
        set_equal to ax for use with subsequent functions
        ------

        fig = Figure to use
        rows = Vertical number of plots
        columns = Horizontal number of plots
        plot_num = Mumber of plot.
        ------
        Returns axes object

        """
        ax = fig.add_subplot(rows,columns,plot_num)
        return ax

    def y_axis_setup(self,ax,min_,max_,interval=1):
        """
        easier y_axis_setup
        ------
        ax = set to ax to use
        min_ = y-axis minimum
        max_ = y-axis maximum
        interval = interval for the axis
        ------
        Returns set y-axis

        """
        yinterval = ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(interval))
        ylim = ax.set_ylim(min_,max_)
        return yinterval, ylim


    def x_axis_setup(self,ax,min_,max_,interval=1):
        """
        easier x_axis_setup
        ------
        ax = set to ax to use
        min_ = x-axis minimum
        max_ = x-axis maximum
        interval = interval for the axis
        ------
        Returns set x-axis

        """
        xinterval = ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(interval))
        xlim = ax.set_xlim(min_,max_)
        return xinterval,xlim


    def citations(self,ax,source,chart_tag,x=0,source_y=-.4,chart_tag_y=-.5,fontsize=14,color='black',alpha=.4):
        """
        Text objets for source and creditation
        ------
        ax = set to ax to use
        source = text indicating your source
        chart_tag = text indicating your creditation
        x = x-position of source and chart_tag
        source_y = y position of source
        chart_tag_y = y position of chart_tag
        fontsize = fontsize for source and chart_tag
        color = color of of source and chart_tag
        alpha = transparency
        ------
        Returns source and creditation text

        """
        source = ax.text(x,source_y,source,transform=ax.transAxes,fontsize=fontsize,color=color,alpha=alpha)
        chart_tag = ax.text(x,chart_tag_y,chart_tag,transform=ax.transAxes,fontsize=fontsize,color=color,alpha=alpha)
        return source, chart_tag

    def patch_adder(self,ax, xy=(0,0),width=1,height=1,facecolor='#f0f0f0',alpha=1):
        """
        Adds a rectangular patch to the chart
        ------
        ax = set to ax to use
        xy = bottom left of rectangular
        width = width proportion for patch to cover
        height = height proportion for patch to cover
        facecolor = color of patch
        alpha = patch transparency
        ------
        Returns rectangular patch

        """
        patch = ax.add_patch(patches.Rectangle(xy, width=width,height=height,facecolor=facecolor,alpha=alpha,transform=ax.transAxes))
        return patch

    def tick_params_(self,ax,axis='both',which='major',fontsize=16,labelcolor='#969696'):
        """
        Set global tick parameters
        ------
        ax :
            set to ax to use

        axis : {‘x’, ‘y’, ‘both’}
            Axis to set

        which : {‘major’, ‘minor’, ‘both’}
            Tick marks to set arguments to

        fontsize:
            Font size for axis ticks

        labelcolor:
            Color for ticks
        ------
        Returns set tick parameters

        """
        tick_overall_set = ax.tick_params(axis=axis, which=which, labelsize=fontsize,labelcolor='#969696')
        return tick_overall_set


def chart_save(name,dpi=100,transparent=False):
    plt.savefig(name,bbox_inches = 'tight', dpi = dpi, pad_inches = .25,transparent=transparent)

def random_alphabet(count):
    return [random.choice(string.ascii_letters[0:26]) for item in range(count)]
