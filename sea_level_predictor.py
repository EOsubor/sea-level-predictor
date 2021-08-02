import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x1, y1 = df['Year'], df['CSIRO Adjusted Sea Level']

    fig, ax = plt.subplots(figsize=(12,7))
    ax.scatter(x=x1, y=y1)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x1, y1)

    line_x = np.arange(x1.min(), 2051)
    line_y = slope*line_x + intercept
    ax.plot(line_x, line_y)

    # Create second line of best fit
    df_2000 = df.loc[df['Year'] >= 2000]
    x2, y2 = df_2000['Year'], df_2000['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x2, y2)
    line_x2 = np.arange(2000, 2051)
    line_y2 = (slope*line_x2) + intercept
    ax.plot(line_x2, line_y2, 'green')

    # Add labels and title
    ax.set(xlabel='Year', ylabel='Sea Level (inches)', title='Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()