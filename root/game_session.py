from tkinter import *
import pandas as pd
import main_menu as gs_mm
from tkinter import messagebox
from time import sleep
import json
import random

class game_char():
    def __init__(self, master, image_path, row_no, column_no):
        char = Label(master, image = image_path)
        char.grid(row = row_no, column = column_no)

def character_selection():
    return random.randint(0,23)

user_character = character_selection()
machine_character = character_selection()

f = open('profiles/admin.json')
profile = json.load(f)

df = pd.read_json('characters/standard_game/standard_game_df.json')

def run_game_session():
    game_session = Tk()

    column_input = StringVar()
    value_input = StringVar()
    machine_question = StringVar()
    user_guess = StringVar()

    def return_main_menu():
        game_session.destroy()
        gs_mm.run_main_menu()
        pass

    def main_reset_game():
        messagebox.showinfo('Game restarted', 'The game was restarted')
        profile['game_resets'] += 1
        json.dump(profile, open('profiles/admin.json', 'w'))
        reset_game()
        pass

    def reset_game():
        global df
        df = pd.read_json('characters/standard_game/standard_game_df.json')
        user_guess.set('')
        yes_button['state'] = DISABLED
        no_button['state'] = DISABLED
        continue_button['state'] = ACTIVE
        pass

    def user_turn():
        column_selection = column_input.get()
        user_criteria = value_input.get()
        yes_button['state'] = ACTIVE
        no_button['state'] = ACTIVE
        continue_button['state'] = DISABLED
        ia_filtering(column_selection, user_criteria)
        computer_winning()
        if len(df.axes[0]) != 24:
            user_guess.set(df['name'])
        else:
            user_guess.set('')
        pass
    
    def confirm_mq():
        computer_operator = '=='
        computer_turn(computer_operator)
        pass

    def negate_mq():
        computer_operator = '!='
        computer_turn(computer_operator)
        pass
    
    def computer_turn(operator):
        yes_button['state'] = DISABLED
        no_button['state'] = DISABLED
        continue_button['state'] = ACTIVE
        print (operator)
        pass

    def ia_filtering(column_name,criteria):
        global df
        df = df.loc[df[column_name] == criteria]
        pass

    def computer_winning():
        global df
        if len(df.axes[0]) == 1:
            df.reset_index(drop = True, inplace = True)
            character = df['name'].values[0]
            messagebox.showinfo('Winner!', ('The computer won this round\nYour character is {}'.format(character)))
            profile['losses'] += 1
            json.dump(profile, open('profiles/admin.json', 'w'))
            reset_game()
        pass

    def ia_question():
        pass

    title = Label(game_session, text = 'Guess Who on Python')
    title.grid(row = 0, columnspan = 8)
    
    char_0 = PhotoImage(file = r'characters/standard_game/Alex.png')
    char_1 = PhotoImage(file = r'characters/standard_game/Alfred.png')
    char_2 = PhotoImage(file = r'characters/standard_game/Anita.png')
    char_3 = PhotoImage(file = r'characters/standard_game/Anne.png')
    char_4 = PhotoImage(file = r'characters/standard_game/Bernard.png')
    char_5 = PhotoImage(file = r'characters/standard_game/Bill.png')
    char_6 = PhotoImage(file = r'characters/standard_game/Charles.png')
    char_7 = PhotoImage(file = r'characters/standard_game/Claire.png')
    char_8 = PhotoImage(file = r'characters/standard_game/David.png')
    char_9 = PhotoImage(file = r'characters/standard_game/Eric.png')
    char_10 = PhotoImage(file = r'characters/standard_game/Frans.png')
    char_11 = PhotoImage(file = r'characters/standard_game/George.png')
    char_12 = PhotoImage(file = r'characters/standard_game/Herman.png')
    char_13 = PhotoImage(file = r'characters/standard_game/Joe.png')
    char_14 = PhotoImage(file = r'characters/standard_game/Maria.png')
    char_15 = PhotoImage(file = r'characters/standard_game/Max.png')
    char_16 = PhotoImage(file = r'characters/standard_game/Paul.png')
    char_17 = PhotoImage(file = r'characters/standard_game/Peter.png')
    char_18 = PhotoImage(file = r'characters/standard_game/Philip.png')
    char_19 = PhotoImage(file = r'characters/standard_game/Richard.png')
    char_20 = PhotoImage(file = r'characters/standard_game/Robert.png')
    char_21 = PhotoImage(file = r'characters/standard_game/Sam.png')
    char_22 = PhotoImage(file = r'characters/standard_game/Susan.png')
    char_23 = PhotoImage(file = r'characters/standard_game/Tom.png')

    character_1 = game_char(game_session, char_0, 1, 0)
    character_2 = game_char(game_session, char_1, 1, 1)
    character_3 = game_char(game_session, char_2, 1, 2)
    character_4 = game_char(game_session, char_3, 1, 3)
    character_5 = game_char(game_session, char_4, 1, 4)
    character_6 = game_char(game_session, char_5, 1, 5)
    character_7 = game_char(game_session, char_6, 1, 6)
    character_8 = game_char(game_session, char_7, 1, 7)
    character_9 = game_char(game_session, char_8, 2, 0)
    character_10 = game_char(game_session, char_9, 2, 1)
    character_11= game_char(game_session, char_10, 2, 2)
    character_12 = game_char(game_session, char_11, 2, 3)
    character_13 = game_char(game_session, char_12, 2, 4)
    character_14 = game_char(game_session, char_13, 2, 5)
    character_15 = game_char(game_session, char_14, 2, 6)
    character_16 = game_char(game_session, char_15, 2, 7)
    character_17 = game_char(game_session, char_16, 3, 0)
    character_18 = game_char(game_session, char_17, 3, 1)
    character_19= game_char(game_session, char_18, 3, 2)
    character_20 = game_char(game_session, char_19, 3, 3)
    character_21 = game_char(game_session, char_20, 3, 4)
    character_22 = game_char(game_session, char_21, 3, 5)
    character_23 = game_char(game_session, char_22, 3, 6)
    character_24 = game_char(game_session, char_23, 3, 7)

    reset_button = Button(game_session, text = 'Reset game', command = main_reset_game)
    reset_button.grid(row = 0, column = 8, sticky = 'E')
    return_button = Button(game_session, text = 'Return to Main Menu', command = return_main_menu)
    return_button.grid(row = 0, column = 9, sticky = 'E')

    machine_output = Label(game_session, textvariable = machine_question)
    machine_output.grid(row = 1, column = 8)
    yes_button = Button(game_session, text = 'Yes', command = confirm_mq, state = DISABLED)
    yes_button.grid(row = 1, column = 9, sticky = 'W')
    no_button = Button(game_session, text = 'No', command = negate_mq, state = DISABLED)
    no_button.grid(row = 1, column = 9, sticky = 'E')

    user_input_title = Label(game_session, text = 'User console')
    user_input_title.grid(row = 2, column = 8, columnspan = 2, sticky = 'N')
    user_input_column = Entry(game_session, textvariable = column_input)
    user_input_column.grid(row = 2, column = 8)
    user_input_value = Entry(game_session, textvariable = value_input)
    user_input_value.grid(row = 2, column = 9)

    continue_button = Button(game_session, text = 'Ask question', command = user_turn)
    continue_button.grid(row = 2, column = 9, sticky = 'S')

    #admin console
    char_assignation_title = Label(game_session, text = 'Your character is...')
    char_assignation_title.grid(row = 0, column = 10)
    char_on_game_value = Label(game_session, image = eval('char_' + str(user_character)))
    char_on_game_value.grid(row = 1, column = 10)

    char_assignation_title = Label(game_session, text = 'Computer character is...')
    char_assignation_title.grid(row = 0, column = 11)
    char_on_game_value = Label(game_session, image = eval('char_' + str(machine_character)))
    char_on_game_value.grid(row = 1, column = 11)
    user_guess_label = Label(game_session, textvariable = user_guess)
    user_guess_label.grid(row = 2, column = 11, rowspan = 2)

    return game_session.mainloop()

if __name__ == '__main__':
    run_game_session()