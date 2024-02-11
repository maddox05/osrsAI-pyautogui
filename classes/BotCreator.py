"""BotCreator is an abstract class which is used to then create other usable bot types"""
from definitions import *
from pyclick import HumanClicker


class BotCreator:
    """
    Creates an instance of a bot. Bot must have a type, location, username, password, and bank pin.

    Bot cannot be just a "Bot Creator" it must be a specific type of bot. BotCreator is an abstract class/interface.
    """

    fires_made = 0  # static
    times_banked = 0  # static
    trees_chopped = 0  # static

    last_tree_chopped = None  # static I think

    try:
        hc = HumanClicker()  # init human clicker # everybody needs a clicker lol
    except:
        print("Failed to initialize human clicker (open a issue on github)")
        print(FATAL_ERROR)
        time.sleep(5)
        quit()

    def __init__(self, btype, location, username, password, bank_pin):
        self.btype = btype
        self.location = location
        self.username = username
        self.password = password
        self.pin = bank_pin

    def login(self):
        pass

    def logout(self):
        pass

    def getLocation(self):
        return self.location

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getTimesBanked(self):
        return self.times_banked

    def addTimesBanked(self):
        self.times_banked += 1

    def getLastTreeChopped(self):
        return self.last_tree_chopped

    def setLastTreeChopped(self, tree):
        self.last_tree_chopped = tree

    def addTreeChopped(self):
        self.trees_chopped += 1
