import pandas as pd
#virtual environment is airbnbenv

listing = pd.read_csv('listing2.csv')

def remove_rows_with_missing_rating():
    listing.dropna()



