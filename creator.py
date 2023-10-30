from definitions import *


class BotCreator:
    """
    Used to create different instances of the bot, not fully implemented yet
    """
    # fires_made = 0 # not used yet
    times_banked = 0

    def __init__(self, location, username, password, bank_pin):
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




