import pandas as pd
import random

df = pd.read_json('characters/standard_game/standard_game_df.json')

columns_to_select = ['name', 'gender', 'hat', 'hair_color', 'hair_length', 'brown_size', 'glasses', 'eye_color', 'nose_size', 'ear_rings', 'mustache', 'mouth_size', 'beard', 'bonnet', 'chaps']

gender_list = ['male', 'female']
hair_color_list = ['black', 'red', 'yellow', 'brown', 'white']
hair_length_list = ['short', 'long', 'none']
smallbig_list = ['small', 'big']
truefalse_list = [True, False]
eye_color_list = ['brown', 'blue']

try_again = 'yes'

def character_selection():
    return random.randint(0,23)

def user_round(column_name,criteria):
    global df
    df = df.loc[df[column_name] == criteria]
    return df

def print_result():
    global df
    return print (df)

def computer_turn():
    column_selection = input()
    user_criteria = input()
    user_round(column_selection, user_criteria)
    print_result()
    pass