
import pandas as pd
import numpy as np

class SLDataFrame:
    def __init__(self, df): #constructor defining the dataframe ****
        self.df = df

    # nicks code for number of total cells (really simple)
    def num_cells(self):
        return self.shape[0] * self.shape[1]  # total data points

    # my code for null_count return (should be an int by default)
    def null_count(self):
        return self.df.isnull().sum().sum()

    # total count of unique 
    def count_unique(self):
        return self.df.isunique().sum()

    # total count of unique in a specific column
    def unique_count(self, col_name):
        return self.df[col_name].isunique().sum()

    # percentage of unique in a particular column
    def unique_percentage(self, col_name):
        return self.unique_count(col_name) / len(self.df) * 100

    # for dropping high cardinality columns
    def high_card_drop(self):
        for col in self.df.columns:
            if self.unique_percentage(col) > 50:
                self.df.drop(columns=col, inplace=True)

    # Train test split on dataframe : 

    # def train_test_split(self, frac):
    #     frac = round(len(self.df)*frac)
    # train = self.df[:frac]
    # test = self.df[frac:]
    #     return train, test