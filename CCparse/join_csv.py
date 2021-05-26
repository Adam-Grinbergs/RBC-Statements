import pandas as pd
import os
from .df_format import format_all
from tqdm import tqdm

def read_and_format(csv_path: str, file: str) -> pd.DataFrame:
    """Reads and structures Tabula's output csv file into a pandas
    dataframe."""
    df = pd.read_csv(
        os.path.join(csv_path, file), index_col=0,
        engine='python', warn_bad_lines=False,
        error_bad_lines=False, header=1
        )
    df = format_all(df, file)
    return df

def df_from_csvs(csv_path: str) -> pd.DataFrame:
    """Takes the path of the output CSVs, and joins them"""
    li = []
    for file in tqdm(os.listdir(csv_path)):
        if file.endswith('.csv'):
            if os.path.getsize(os.path.join(csv_path, file)) > 0:
                df = read_and_format(csv_path, file)
                if df is not None:
                    li.append(df)
    frame = pd.concat(li, axis=0, ignore_index=True)
    return frame
