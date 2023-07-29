import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
# filter via the datetime
df["date"] = pd.to_datetime(df["date"])

# set index to "date"
df.set_index("date", inplace=True)

# Clean data
df = df.loc[
    # filter the data [2.5% - 97.5%]
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # Draw line
    fig, ax = plt.subplots(figsize=(20, 5))
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    plt.plot(df.index, df["value"])

    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    # gives me the year and converts the month number to the name of the month
    df_bar["Years"] = df.index.year
    df_bar["Months"] = df.index.month_name()

    # create a grouping of categories and apply a function to the categories
    df_bar = pd.DataFrame(df_bar.groupby(["Years", "Months"], sort=False)["value"].mean().round().astype(int))
    # rename column
    df_bar = df_bar.rename(columns={"value": "Mean Values"})

    """
    When we look at the smaller dataframe, it might still carry the row index of the original dataframe.
    If the original index are numbers, now we have indexes that are not continuous.
    Well, pandas has reset_index() function. 
    So to reset the index to the default integer index beginning at 0.
    """
    df_bar = df_bar.reset_index()

    # Draw bar plot
    # Pivot the DF so that there's a column for each month, each row\
    # represents a year, and the cells have the mean page views for the\
    # respective year and month
    df_pivot = pd.pivot_table(df_bar, values="Mean Values", index="Years", columns="Months")

    # Plot a bar chart using the DF
    ax = df_pivot.plot(kind="bar", edgecolor="black")

    # Get a Matplotlib figure from the axes object for formatting purposes
    fig = ax.get_figure()

    # Change the plot dimensions (width, height)
    fig.set_size_inches(8, 7)

    # Change the axes labels
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                       'November', 'December'], title="Months")
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
