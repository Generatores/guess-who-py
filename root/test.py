import pandas as pd

df = pd.read_json('characters/standard_game/standard_game_df.json')

df = df.loc[df['gender'] == 'male']

print (df)

