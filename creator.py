class BotCreator:
    trees_chopped = 0
    fires_made = 0

    def __init__(self, location, username, password):
        self.location = location
        self.username = username
        self.password = password

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

    def getFiresMade(self):
        return self.fires_made

    def getTreesChopped(self):
        return self.trees_chopped

    def addTreeChopped(self):
        self.trees_chopped += 1
