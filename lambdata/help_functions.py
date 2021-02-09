# find nulls in dataframe


# a function to return a null count
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