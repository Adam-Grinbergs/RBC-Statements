from tabula import io
import os
from .join_csv import df_from_csvs
import sys

# The path for the PDFs to sit in.
input_path = './files'
# The output path.
output_path = '../CC'


def parse():
    """Convert PDFs to CSV, then structure and combine"""
    # This converts each PDF into a unique csv.
    #io.convert_into_by_batch(input_path, output_format='csv', pages='all')
    # Creates one big dataframe from the output.
    df = df_from_csvs(input_path)
    # Change this name if you want your CSV to be named something else.
    df.to_csv(os.path.join(output_path, 'output.csv'), index=False)