import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid', rc={'figure.figsize':(20,8)})

# Reads csv files
companies = pd.read_csv('data/companies.tsv', sep='\t')
deals = pd.read_csv('data/deals.tsv', sep='\t')
sectors = pd.read_csv('data/sectors.tsv', sep='\t')
contacts = pd.read_csv('data/contacts.tsv', sep='\t')

# Removes spaces from column names
new_columns = dict(zip(contacts.columns, contacts.columns.str.strip()))
contacts.rename(new_columns, axis=1, inplace=True)

def first_output() -> pd.DataFrame:
    """Generates a dataframe that enables the creation and analysis of
    the sold value by month and by contact. Also creates a csv file in
    output directory

    Returns:
        pd.DataFrame: Dataframe containing contact name, deal value and month
    """

    contacts_deals = deals.merge(contacts, on='contactsId', how='left')
    # Creates a date column containing the 'month'/YY
    contacts_deals['monthYear'] = pd.to_datetime(contacts_deals['dealsDateCreated'])
    contacts_deals['monthYear'] = contacts_deals['monthYear'].dt.strftime('%b/%y')
    # Filters columns needed to create the sold value by month and by contact
    needed_columns = ['contactsName', 'dealsPrice', 'monthYear']
    first_output = contacts_deals[needed_columns]

    first_output.to_csv('output/first_output.csv', index=False)

    return first_output

def second_output() -> pd.DataFrame:
    """Creates a dataframe containing information about the percentual sold 
    value for each sector of the industry. Also exports this csv file to
    output directory

    Returns:
        pd.DataFrame: Dataframe containing the percentage of value by sector
    """

    companies_deals = deals.merge(companies[['companiesId', 'sectorKey']],
                                             on='companiesId', how='left')
    sector_deals = companies_deals.merge(sectors, on='sectorKey', how='left')

    sector_value = sector_deals.groupby('sector').sum().reset_index()
    sector_percent = sector_value['dealsPrice'] / sector_value['dealsPrice'].sum()
    sector_value['dealsPercent'] = sector_percent.round(3)
    sector_value.sort_values('dealsPercent', ascending=False, inplace=True)

    sector_value[['sector', 'dealsPercent']].to_csv('output/second_output.csv',
                                                    index=False)
    pass


if __name__ == '__main__':
    try:
        os.mkdir('output')
    except FileExistsError:
        pass
    first_output()
    second_output()
