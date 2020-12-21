from tkinter import *

turn_counter = 0
active_turn = 'Your turn'

def run_game_session():
    game_session = Tk()

    def turn_color():
        if active_turn == 'Computer`s turn':
            return 'red'
        return 'green'

    def next_turn():
        global turn_counter
        global active_turn
        if turn_counter == 0:
            active_turn = 'Computer`s turn'
            turn_counter += 1
            print (active_turn)
        else:
            active_turn = ('Your turn')
            turn_counter -= 1
            print (active_turn)

    title = Label(game_session, text = 'Guess Who on Python')
    title.grid(row = 0, columnspan = 8)

    char_1 = PhotoImage(file = r'characters/standard_game/Alfred.png')
    char_2 = PhotoImage(file = r'characters/standard_game/Alfred.png')
    char_3 = PhotoImage(file = r'characters/standard_game/Anita.png')
    char_4 = PhotoImage(file = r'characters/standard_game/Anne.png')
    char_5 = PhotoImage(file = r'characters/standard_game/Bernard.png')
    char_6 = PhotoImage(file = r'characters/standard_game/Bill.png')
    char_7 = PhotoImage(file = r'characters/standard_game/Charles.png')
    char_8 = PhotoImage(file = r'characters/standard_game/Claire.png')
    char_9 = PhotoImage(file = r'characters/standard_game/David.png')
    char_10 = PhotoImage(file = r'characters/standard_game/Eric.png')
    char_11 = PhotoImage(file = r'characters/standard_game/Frans.png')
    char_12 = PhotoImage(file = r'characters/standard_game/George.png')
    char_13 = PhotoImage(file = r'characters/standard_game/Herman.png')
    char_14 = PhotoImage(file = r'characters/standard_game/Joe.png')
    char_15 = PhotoImage(file = r'characters/standard_game/Maria.png')
    char_16 = PhotoImage(file = r'characters/standard_game/Max.png')
    char_17 = PhotoImage(file = r'characters/standard_game/Paul.png')
    char_18 = PhotoImage(file = r'characters/standard_game/Peter.png')
    char_19 = PhotoImage(file = r'characters/standard_game/Philip.png')
    char_20 = PhotoImage(file = r'characters/standard_game/Richard.png')
    char_21 = PhotoImage(file = r'characters/standard_game/Robert.png')
    char_22 = PhotoImage(file = r'characters/standard_game/Sam.png')
    char_23 = PhotoImage(file = r'characters/standard_game/Susan.png')
    char_24 = PhotoImage(file = r'characters/standard_game/Tom.png')

    character_1 = Label(game_session, image = char_1)
    character_1.grid(row = 1, column = 0)
    character_2 = Label(game_session, image = char_2)
    character_2.grid(row = 1, column = 1)
    character_3 = Label(game_session, image = char_3)
    character_3.grid(row = 1, column = 2)
    character_4 = Label(game_session, image = char_4)
    character_4.grid(row = 1, column = 3)
    character_5 = Label(game_session, image = char_5)
    character_5.grid(row = 1, column = 4)
    character_6 = Label(game_session, image = char_6)
    character_6.grid(row = 1, column = 5)
    character_7 = Label(game_session, image = char_7)
    character_7.grid(row = 1, column = 6)
    character_8 = Label(game_session, image = char_8)
    character_8.grid(row = 1, column = 7)
    character_9 = Label(game_session, image = char_9)
    character_9.grid(row = 2, column = 0)
    character_10 = Label(game_session, image = char_10)
    character_10.grid(row = 2, column = 1)
    character_11 = Label(game_session, image = char_11)
    character_11.grid(row = 2, column = 2)
    character_12 = Label(game_session, image = char_12)
    character_12.grid(row = 2, column = 3)
    character_13 = Label(game_session, image = char_13)
    character_13.grid(row = 2, column = 4)
    character_14 = Label(game_session, image = char_14)
    character_14.grid(row = 2, column = 5)
    character_15 = Label(game_session, image = char_15)
    character_15.grid(row = 2, column = 6)
    character_16 = Label(game_session, image = char_16)
    character_16.grid(row = 2, column = 7)
    character_17 = Label(game_session, image = char_17)
    character_17.grid(row = 3, column = 0)
    character_18 = Label(game_session, image = char_18)
    character_18.grid(row = 3, column = 1)
    character_19 = Label(game_session, image = char_19)
    character_19.grid(row = 3, column = 2)
    character_20 = Label(game_session, image = char_20)
    character_20.grid(row = 3, column = 3)
    character_21 = Label(game_session, image = char_21)
    character_21.grid(row = 3, column = 4)
    character_22 = Label(game_session, image = char_22)
    character_22.grid(row = 3, column = 5)
    character_23 = Label(game_session, image = char_23)
    character_23.grid(row = 3, column = 6)
    character_24 = Label(game_session, image = char_24)
    character_24.grid(row = 3, column = 7)
    
    turn_indicator = Label(game_session, text = active_turn, fg = turn_color())
    turn_indicator.grid(row = 0, column = 8, columnspan = 2)

    machine_output_title = Label(game_session, text = 'Machine output')
    machine_output_title.grid(row = 1, column = 8)
    machine_output_text = Label(game_session, text = 'Machine output goes right here...')
    machine_output_text.grid(row = 1, column = 9)

    user_input_title = Label(game_session, text = 'User input')
    user_input_title.grid(row = 3, column = 8)
    user_input_class_title = Label(game_session, text = 'User input goes right here...')
    user_input_class_title.grid(row = 3, column = 9)

    continue_button = Button(game_session, text = 'Continue...', command = next_turn)
    continue_button.grid(row = 2, column = 8)
    continue_button = Button(game_session, text = 'Surrender :(')
    continue_button.grid(row = 2, column = 9)

    game_session.mainloop()
    pass

if __name__ == '__main__':
    run_game_session()