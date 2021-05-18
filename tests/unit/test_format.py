"""I should test whether I am able to drop the columns I want to drop,
and whether the column names end up being the appropriate ones"""

import unittest

"""Functions to test: fcols, f_date, f_amt, f_vendor"""
"""How to test them: 
1. Fcols - give it a dataframe of the type that I'm expecing (3 or more cols from tabula)
and see if it properly drops the extra columns and returns a df
with 3 columns, and also maybe test to ensure that it handles the weird cases
2. F_date - give it a dataframe of the type that I'm expecting, which is the 
3-column formatted dataframe. The test should ensure that fdate returns 
a proper date column with no na values.
3. f_amt - should take in the output of the f_date function and drop na
rows in amount as appropriate
4. f_vendor - should ensure that the function removes the payment
thank you values from the csv file."""