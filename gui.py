"""
Gui to create a Bot Creator object.
"""
import tkinter as tk
import threading
from mapletree import MapleCutter

bot_type = ["Tree Chopping", "x", "x"]
tree_locations = ["Seers Village", "x", "x"]


def guiStart():
    root = tk.Tk()
    root.geometry("230x320")

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
        print("submitting")
        print(f"Type: {types_var.get()}")
        print(f"Location: {locations_var.get()}")
        print(f"Username: {username_var.get()}")
        print(f"Password: {password_var.get()}")
        print(f"Bank Pin: {bank_pin_var.get()}")
        root.destroy()
        # create bot object

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack(pady=5)


    root.title("Bot Creator")
    root.mainloop()


threading.Thread(target=guiStart()).start()
