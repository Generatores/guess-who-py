from tkinter import *
import pandas as pd
import basic_functions as gs_bf
from time import sleep

#version:       0.1.0
#created by:    Bruno Ruiz S

user_character = gs_bf.character_selection()
machine_character = gs_bf.character_selection()

df = pd.read_json('characters/standard_game/standard_game_df.json')

def run_game_session():
    game_session = Tk()

    column_input = StringVar()
    value_input = StringVar()
    machine_question = StringVar()
    user_guess = StringVar()
    ia_answer = StringVar()

    def user_turn():
        column_selection = column_input.get()
        user_criteria = value_input.get()
        yes_button['state'] = ACTIVE
        no_button['state'] = ACTIVE
        continue_button['state'] = DISABLED
        ia_filtering(column_selection, user_criteria)
        computer_winning()
        user_guess.set(df['name'])
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

    #Start of IA functions
    def ia_filtering(column_name,criteria):
        global df
        df = df.loc[df[column_name] == criteria]
        pass

    def computer_winning():
        global df
        if len(df.axes[0]) == 1:
            ia_answer.set('Your character is ' + df['name'])
        pass

    def ia_question():
        pass
    #End of IA functions

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

    character_1 = Label(game_session, image = char_0)
    character_1.grid(row = 1, column = 0)
    character_2 = Label(game_session, image = char_1)
    character_2.grid(row = 1, column = 1)
    character_3 = Label(game_session, image = char_2)
    character_3.grid(row = 1, column = 2)
    character_4 = Label(game_session, image = char_3)
    character_4.grid(row = 1, column = 3)
    character_5 = Label(game_session, image = char_4)
    character_5.grid(row = 1, column = 4)
    character_6 = Label(game_session, image = char_5)
    character_6.grid(row = 1, column = 5)
    character_7 = Label(game_session, image = char_6)
    character_7.grid(row = 1, column = 6)
    character_8 = Label(game_session, image = char_7)
    character_8.grid(row = 1, column = 7)
    character_9 = Label(game_session, image = char_8)
    character_9.grid(row = 2, column = 0)
    character_10 = Label(game_session, image = char_9)
    character_10.grid(row = 2, column = 1)
    character_11 = Label(game_session, image = char_10)
    character_11.grid(row = 2, column = 2)
    character_12 = Label(game_session, image = char_11)
    character_12.grid(row = 2, column = 3)
    character_13 = Label(game_session, image = char_12)
    character_13.grid(row = 2, column = 4)
    character_14 = Label(game_session, image = char_13)
    character_14.grid(row = 2, column = 5)
    character_15 = Label(game_session, image = char_14)
    character_15.grid(row = 2, column = 6)
    character_16 = Label(game_session, image = char_15)
    character_16.grid(row = 2, column = 7)
    character_17 = Label(game_session, image = char_16)
    character_17.grid(row = 3, column = 0)
    character_18 = Label(game_session, image = char_17)
    character_18.grid(row = 3, column = 1)
    character_19 = Label(game_session, image = char_18)
    character_19.grid(row = 3, column = 2)
    character_20 = Label(game_session, image = char_19)
    character_20.grid(row = 3, column = 3)
    character_21 = Label(game_session, image = char_20)
    character_21.grid(row = 3, column = 4)
    character_22 = Label(game_session, image = char_21)
    character_22.grid(row = 3, column = 5)
    character_23 = Label(game_session, image = char_22)
    character_23.grid(row = 3, column = 6)
    character_24 = Label(game_session, image = char_23)
    character_24.grid(row = 3, column = 7)

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
    
    computer_answer = Label(game_session, textvariable = ia_answer)
    computer_answer.grid(row = 3, column = 8, columnspan = 2)

    return game_session.mainloop()

if __name__ == '__main__':
    run_game_session()