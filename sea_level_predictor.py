import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress



def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    fig, ax = plt.subplots(figsize =(12,12))

    plt.scatter(x,y)

    # Create first line of best fit
    reg = linregress(x,y)
    x_forcast = pd.Series(([i for i in range(1880, 2051)]))
    y_forcast = reg.slope * x_forcast + reg.intercept
    plt.plot(x_forcast, y_forcast, 'r')

    
    # Create second line of best fit
    new_df = df.loc[df['Year'] >= 2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    res_2 = linregress(new_x, new_y)
    x_forcast2 = pd.Series([i for i in range(2000, 2051)])
    y_forcast2 = res_2.slope * x_forcast2 + res_2.intercept
    plt.plot(x_forcast2, y_forcast2, 'green')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()