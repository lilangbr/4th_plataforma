from get_object_api import get_txt_to_df

df = get_txt_to_df('../src/heroes.txt')

def four_laps_completed(dataframe):
    return dataframe[(dataframe['Lap'] >= 4)]
print (four_laps_completed(df))

