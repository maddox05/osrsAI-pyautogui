"""
Gui to create a Bot Creator object.
"""
import tkinter as tk
import threading

from BotCreator import BotCreator


def guiStart() -> dict:
    bot_type = ["Tree Chopping", "x", "x"]
    tree_locations = ["Seers Village", "x", "x"]
    root = tk.Tk()

    root.geometry("250x340")

    types_var = tk.StringVar()
    types_var.set(bot_type[0])
    type_selection = tk.OptionMenu(root, types_var, *bot_type)
    type_selection.pack(pady=10)

    locations_var = tk.StringVar()
    if types_var.get() == "Tree Chopping":  # will just instantly set it, should loop to keep checking
        locations_var.set(tree_locations[0])
        locations_selection = tk.OptionMenu(root, locations_var, *tree_locations)
        locations_selection.pack(pady=10)

    username_label = tk.Label(root, text="Username")
    username_label.pack()
    username_var = tk.StringVar()
    username = tk.Entry(root, textvariable=username_var)
    username.pack(pady=10)

    password_label = tk.Label(root, text="Password")
    password_label.pack()
    password_var = tk.StringVar()
    password = tk.Entry(root, textvariable=password_var)
    password.pack(pady=10)

    bank_pin_label = tk.Label(root, text="Bank Pin")
    bank_pin_label.pack()
    bank_pin_var = tk.StringVar()
    bank_pin = tk.Entry(root, textvariable=bank_pin_var)
    bank_pin.pack(pady=10)

    # submit button
    def submit():
        # create a submit button
        # check if all fields are filled out

        if len(bank_pin_var.get()) == 4 or len(bank_pin_var.get()) == 0:
            pass
        else:
            print("Bank Pin must be 4 or 0 digits long")
            return  # ends submit and does not quit gui

        if len(username_var.get()) == 0:
            print("Username must be filled out")
            return
        if len(password_var.get()) == 0:
            print("Password must be filled out")
            return
        if types_var.get() == "x":
            print("Type must be selected")
            return
        print("submitting")
        print(f"Type: {types_var.get()}")
        print(f"Location: {locations_var.get()}")
        print(f"Username: {username_var.get()}")
        print(f"Password: {password_var.get()}")
        print(f"Bank Pin: {bank_pin_var.get()}")

        root.destroy()
        root.quit()
        return

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack(pady=5)

    root.title("Bot Creator")
    root.mainloop()
    return {  # return hash map with certain gui choices in it, root main loop stops when submit is clicked
        "types_var": types_var.get(),
        "locations_var": locations_var.get(),
        "username_var": username_var.get(),
        "password_var": password_var.get(),
        "bank_pin_var": bank_pin_var.get()
    }


def mainGUI():
    root = tk.Tk()
    root.geometry("250x340")
    root.title("Info")

    tk.Label(root, text="Times Banked").pack()

    times_banked_var = tk.StringVar()
    times_banked_var.set(BotCreator.times_banked)
    tk.Label(root, textvariable=times_banked_var).pack()

    tk.Label(root, text="Trees Chopped").pack()

    trees_chopped_var = tk.StringVar()
    trees_chopped_var.set(BotCreator.trees_chopped)
    tk.Label(root, textvariable=trees_chopped_var).pack()

    def updateMainGUI():
        times_banked_var.set(BotCreator.times_banked)
        trees_chopped_var.set(BotCreator.trees_chopped)
        root.after(1000, updateMainGUI)

    threading.Thread(target=updateMainGUI()).start()

    root.mainloop()


