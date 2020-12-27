from tkinter import *
import json, new_profile_title

def run_options_menu():
    options_menu = Tk()

    def start_new_profile():
        new_profile.run_new_profile()
        pass

    f = open('profiles/admin.json')
    user_profile = json.load(f)

    profile_title = Label(options_menu, text = 'Profile Record')
    profile_title.grid(row = 0, column = 0, columnspan = 2)

    profile_name_label = Label(options_menu, text = 'Profile Name:')
    profile_name_label.grid(row = 1, column = 0, sticky = 'W')
    profile_name = Label(options_menu, text = user_profile['name'])
    profile_name.grid(row = 1, column = 1)
    profile_creation_label = Label(options_menu, text = 'Playing since:')
    profile_creation_label.grid(row = 2, column = 0, sticky = 'W')
    profile_creation = Label(options_menu, text = user_profile['creation_date'])
    profile_creation.grid(row = 2, column = 1)
    profile_wins_label = Label(options_menu, text = 'Games won:')
    profile_wins_label.grid(row = 3, column = 0, sticky = 'W')
    profile_wins = Label(options_menu, text = user_profile['wins'])
    profile_wins.grid(row = 3, column = 1)
    profile_losses_label = Label(options_menu, text = 'Games lost:')
    profile_losses_label.grid(row = 4, column = 0, sticky = 'W')
    profile_losses = Label(options_menu, text = user_profile['losses'])
    profile_losses.grid(row = 4, column = 1)
    profile_ratio_label = Label(options_menu, text = 'Win/Lose ratio:')
    profile_ratio_label.grid(row = 5, column = 0, sticky = 'W')
    profile_ratio = Label(options_menu, text = (user_profile['wins']/user_profile['losses']))
    profile_ratio.grid(row = 5, column = 1)

    create_new_profile_button = Button(options_menu, text = 'Create new profile', command = start_new_profile)
    create_new_profile_button.grid(row = 6, column = 0, columnspan = 2)

    return options_menu.mainloop()
    
if __name__ == '__main__':
    run_options_menu()
