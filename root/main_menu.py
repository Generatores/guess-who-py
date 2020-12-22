from tkinter import *
import game_session

#version:       0.1.0
#created by:    Bruno Ruiz S

def run_main_menu():
    main_menu = Tk()

    def start_game():
        main_menu.destroy()
        game_session.run_game_session()
        pass

    active_profile = StringVar()
    active_profile.set('admin')

    against_machine = Radiobutton(main_menu, text = '1 Vs Machine', width = 15, state = DISABLED)
    against_machine.grid(row = 0, column = 0)
    
    against_someone = Radiobutton(main_menu, text = '1 Vs 1', width = 15, state = DISABLED)
    against_someone.grid(row = 0, column = 1)

    start = Button(main_menu, text = 'Start Game!', width = 15, command = start_game)
    start.grid(row = 1, column = 0, columnspan = 2)
    
    profile_name = Label(main_menu, textvariable = active_profile)
    profile_name.grid(row = 2, column = 0, sticky = 'W')

    option_button = Button(main_menu, text = 'Options', width = 15)
    option_button.grid(row = 2, column = 1)

    return main_menu.mainloop()
    

if __name__ == '__main__':
    run_main_menu()