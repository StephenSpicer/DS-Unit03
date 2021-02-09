#a function to return a null count

import typing_extensions


def null_count(df):
    null_count = df.isnull().sum()
    return null_count


# a function to randomize a dataframe
def randomize(df):
     randomizer = np.random.shuffle(DataFrame.values)
    return randomizer 

# train test split function 
def train_test_split(df, seed):
    train = df.sample(frac=0.8, random_state=42)
    test = df.drop(train.index)
    return

# more train test function stuff

#def train_test_split_2(df, seed):
 #   mask = np.random.rand(len(df)) < 0.8
  #  train = df[mask]
   # test = df[~mask]
    #return train, test




#   # Drop features with lots of NaN values
#  df.dropna(axis=1, thresh=len(df)*0.8, inplace=True)

  # Function for dropping high-cardinality columns. 
  # high_card
#def high_card(df):
       # drop_cols = [col for col in df.select_dtypes('object').columns
        #       if df[col].nunique() > 100]
        #df.drop(columns=drop_cols, inplace=True)
       # return df

# going to submit this with 2 functioning functions to see if it works. 