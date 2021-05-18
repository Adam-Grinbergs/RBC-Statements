import pandas as pd
import os


def format_all(df: pd.DataFrame, file: str) -> pd.DataFrame:
    df = f_cols(df)
    if df is None:
        return None
    df = f_date(df, file)
    df = f_amt(df)
    df = f_vendor(df)
    return df


def f_cols(df: pd.DataFrame) -> pd.DataFrame:
    """This function takes in a DataFrame given by Tabula, and removes
    the extra columns that sometimes get thrown into the mix."""
    # Drop everything except the meaningful first columns.
    df.drop(df.iloc[:, 3:], axis=1, inplace=True)
    # Handle Tabula only converting two columns worth of data
    if len(df.columns) < 3:
        return None
    # Rename the columns to later aid in concatenation.
    df.columns = ['date', 'vendor', 'amount']
    return df


def f_date(df: pd.DataFrame, file: str) -> pd.DataFrame:
    """Format the transaction date column."""
    # Add the filename because it contains the year
    df['filename'] = os.path.basename(file)
    # Regex pattern which matches year in the filename.
    pat = r'(20\d\d)'
    # Extract the first year from the filename.
    df['year'] = df['filename'].str.extract(pat)
    # Add the year to the transaction date column.
    df['date'] = df[['date', 'year']].apply(
        lambda x: ' '.join(x.values.astype(str)),
        axis="columns"
        )
    # Convert the transaction date column to datetime.
    df['date'] = pd.to_datetime(
        df['date'].str.lower(), format='%b %d %Y',
        errors='coerce'
        )
    # Drop any non-datetime values from the transaction date.
    df = df.dropna(subset=['date'])
    # Finally get rid of the year and filename columns.
    # because we don't need them anymore.
    df = df.drop(['filename', 'year'], axis='columns')
    return df


def f_amt(df: pd.DataFrame) -> pd.DataFrame:
    # Drop NA values from the amount column.
    df = df.dropna(subset=['amount'])
    return df


def f_vendor(df: pd.DataFrame) -> pd.DataFrame:
    # Drop RBC's Payment Credit, since we are looking at purchases.
    df = df[df["vendor"].str.contains(
        'PAYMENT - THANK YOU / PAIEMENT - MERCI') == False]
    return df
