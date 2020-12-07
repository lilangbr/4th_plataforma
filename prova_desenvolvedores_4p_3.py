from modules_api.get_object_api import get_txt_to_df

df = get_txt_to_df('./src/heroes.txt')
print( type(df))
print(df)
