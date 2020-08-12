import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid', rc={'figure.figsize':(20,8)})

companies = pd.read_csv('data/companies.tsv', sep='\t')
deals = pd.read_csv('data/deals.tsv', sep='\t',
                    index_col='dealsDateCreated',
                    parse_dates=True)
contacts = pd.read_csv('data/contacts.tsv', sep='\t')
sectors = pd.read_csv('data/sectors.tsv', sep='\t')

def value_per_month(df: pd.DataFrame, column: str):
    """Create a plot with the total sold value of each month and save figure
    in output directory

    Args:
        df: Time series dataframe
        column: Name of the numerical column to sum by month
    
    Returns:
    """

    value_by_month = df.resample('MS').sum()
    value_by_month['month'] = value_by_month.index.to_series().dt.strftime('%b/%y')
    # Change the date format to 'mon'/YY
    #value_by_month['month'] = value_by_month['month'].dt.strftime('%b/%y')

    bar_plot = sns.barplot(x='month', y=column,
                           data=value_by_month, color='dodgerblue')

    # Set legend, title and x/y labels
    bar_plot.legend(['Sold Value'])
    bar_plot.set_title('Total Sold Value By Month', fontsize=20)
    bar_plot.set(xlabel='Month/Year',ylabel='Sold Value')

    # Add label to each bar
    for i, bar in enumerate(bar_plot.patches):
        h = bar.get_height()
        bar_plot.text(
            i, # bar index (x coordinate of text)
            h+1000, # y coordinate of text
            '{}'.format(int(h)),  # y label
            ha='center', 
            va='center', 
            size=14)

    # Save plot
    bar_plot.get_figure().savefig('output/sold_value_month.png')

    pass



if __name__ == '__main__':
    try:
        os.mkdir('output')
    except FileExistsError:
        pass
    value_per_month(deals, 'dealsPrice')
