import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x=data["Year"], y=data["CSIRO Adjusted Sea Level"], color="cyan", edgecolors="black")
    x = pd.Series(list(range(1880, 2051)))
    y = pd.Series(list(range(2000, 2051)))

    # Create first line of best fit
    pred_func = linregress(data["Year"], data["CSIRO Adjusted Sea Level"])
    pred_y = lambda x: pred_func.intercept + pred_func.slope * x
    plt.plot(x, pred_y(x), color="red")

    # Create second line of best fit
    new_data = data[data['Year'] > 1999]
    new_pred_func = linregress(new_data['Year'], new_data['CSIRO Adjusted Sea Level'])
    new_pred_y = lambda x: new_pred_func.intercept + new_pred_func.slope * x
    plt.plot(y, new_pred_y(y), color="black")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()