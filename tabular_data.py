import pandas as pd
import csv 
#virtual environment is airbnbenv


def load_listing_file() -> pd.DataFrame:
    df = pd.read_csv("listing2.csv") # loads in the csv file as a pandas data frame
    return df

def remove_rows_with_missing_rating(df: pd.DataFrame) -> pd.DataFrame:  
    df.dropna(subset=['Cleanliness_rate','Accuracy_rate','Location_rate','Check-in_rate','Value_rate'])
    # removes all rows where there is a missing value in any of the ratings columns
    return df

def combine_description_strings(df: pd.DataFrame) -> pd.DataFrame:
    
    return df

def set_default_feature_values(df: pd.DataFrame) -> pd.DataFrame:

    return df

def clean_tabular_data(df: pd.DataFrame) -> pd.DataFrame:
    df = remove_rows_with_missing_rating(df)
    df = combine_description_strings(df)
    df = set_default_feature_values(df)
    return df

def save_listing_file(df: pd.DataFrame) -> None:
    df.to_csv("claen_tabular_data.csv")
    return

if __name__ == "__main__":
    listing = load_listing_file()
    cleaned_listing = clean_tabular_data(listing)
    save_listing_file(cleaned_listing)



