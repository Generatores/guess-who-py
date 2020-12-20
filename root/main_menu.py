from tkinter import *

def run_main_menu():
    main_menu = Tk()

    gamemode_frame = Frame(main_menu)
    gamemode_frame.pack(fill = BOTH, expand = TRUE)
    start_frame = Frame(main_menu)
    start_frame.pack(fill = BOTH, expand = TRUE)
    footer_frame = Frame(main_menu)
    footer_frame.pack(fill = BOTH, expand = TRUE)

    against_machine = Radiobutton(gamemode_frame, text = '1 Vs Machine', width = 15, state = DISABLED)
    against_machine.pack(side = LEFT)
    
    against_someone = Radiobutton(gamemode_frame, text = '1 Vs 1', width = 15)
    against_someone.pack(side = RIGHT)

    start = Button(start_frame, text = 'Start Game!', width = 15)
    start.pack(side = BOTTOM)
    
    user = Label(footer_frame, text = 'Username')
    user.pack(side = LEFT)

    statistics = Button(footer_frame, text = 'View statistics', width = 15)
    statistics.pack(side = RIGHT)
    
    main_menu.mainloop()
    pass

if __name__ == '__main__':
    run_main_menu()