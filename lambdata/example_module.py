""" a module in Lambdata"""

favorite_animals = ['tree frog', 'white rhino', 'zebra']

nullset = ['Nan', 1, 2, 3, 4]

nulldf = pd.DataFrame(nullset)


ODI_runs = {'name': ['Tendulkar', 'Sangakkara', 'Ponting',
                      'Jayasurya', 'Jayawardene', 'Kohli',
                      'Haq', 'Kallis', 'Ganguly', 'Dravid'],
            'runs': [18426, 14234, 13704, 13430, 12650,
                     11867, 11739, 11579, 11363, 10889]}

ODIdf = pd.DataFrame(ODI_runs)

# ODIdf.iloc[,1] = np.NaN