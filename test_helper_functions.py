

import pandas as pd
import numpy as np

import pytest 
from pydataset import data

from lambdata.helper_functions import SLDataFrame as sl 

df = data('titanic')

def test_null():
    """ testing output of null_count"""
    df_null = sl.null_count(df)
    assert isinstance(df_null, np.int64)

def test_num_cells():
    df_count = sl.num_cells(df)
    #assert isinstance(df_count, np.int64)
    assert isinstance(df_count, int)

# Not working right now! 
# def test_unique_count():
#     df_colunique = sl.unique_count(df, 'survived')
#     assert isinstance(df_colunique, int)
#     assert df_colunique.dtype() == np.int64 or int