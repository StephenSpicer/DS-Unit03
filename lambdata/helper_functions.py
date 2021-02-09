# find nulls in dataframe



# a function to return a null count
# null_count

def null_count(df):
    nullcount = df.isnull().sum()
    return nullcount


# a function to randomize a dataframe
# def randomize(df, seed):
    # randomizer = 

# def train_test_split(df, frac=0.8):
#    train = df.len()*frac
#    test = df.len()*(1-frac)
#    return

#   # Drop features with lots of NaN values
#  df.dropna(axis=1, thresh=len(df)*0.8, inplace=True)

  # Function for dropping high-cardinality columns. 
  # high_card
def high_card(df):
        drop_cols = [col for col in df.select_dtypes('object').columns
               if df[col].nunique() > 100]
        df.drop(columns=drop_cols, inplace=True)
        return df

# going to submit this with 2 functioning functions to see if it works. 