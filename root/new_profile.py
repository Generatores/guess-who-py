from tkinter import *
from tkinter import messagebox
import datetime, json

def run_new_profile():
    new_profile = Tk()

    def create_profile():
        name_value = name.get()
        now = str(datetime.datetime.now())
        json_name = 'profiles/' + name_value + '.json'
        json_file = {
            'name' : name_value,
            'creation_date' : now,
            'wins' : 0,
            'losses' : 0
        }
        with open(json_name, 'w') as jsonFile:
            json.dump(json_file, jsonFile)
        messagebox.showinfo('New Profile', 'The profile ' + name_value + ' was created succesfully')
        pass

    new_profile_title = Label(new_profile, text = 'New Profile Form')
    new_profile_title.grid(row = 0, column = 0, columnspan = 2)

    name_label = Label(new_profile, text = 'Profile Name')
    name_label.grid(row = 1, column = 0, sticky = 'W')
    name = Entry(new_profile)
    name.grid(row = 1, column = 1)

    create_profile_button = Button(new_profile, text = 'Create profile', command = create_profile)
    create_profile_button.grid(row = 2, column = 0, columnspan = 2)

    new_profile.mainloop()
    pass

if __name__ == '__main__':
    run_new_profile()