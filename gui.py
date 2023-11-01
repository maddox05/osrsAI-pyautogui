"""
Gui to create a Bot Creator object.
"""
import tkinter
import threading


def guiStart():
    root = tkinter.Tk()

    root.title("Bot Creator")
    root.mainloop()


threading.Thread(target=guiStart()).start()
