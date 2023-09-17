import pyautogui
import random

tree_1_maple_images = ["assets/seers-village-maples/tree-1-maple/tree-maple-1-1.png",
                       "assets/seers-village-maples/tree-1-maple/tree-maple-1-2.png"]

tree_2_maple_images = ["assets/seers-village-maples/tree-2-maple/tree-maple-2-1.png",
                       "assets/seers-village-maples/tree-2-maple/tree-maple-2-2.png"]

tree_3_maple_images = ["assets/seers-village-maples/tree-3-maple/tree-maple-3-1.png"]

tree_4_maple_images = ["assets/seers-village-maples/tree-4-maple/tree-maple-4-1.png",
                       "assets/seers-village-maples/tree-4-maple/tree-maple-4-2.png"]

class BotCreator:
    trees_chopped = 0
    fires_made = 0
    times_banked = 0
    last_tree_chopped = 0

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

    def getFiresMade(self):
        return self.fires_made

    def getTreesChopped(self):
        return self.trees_chopped

    def addTreeChopped(self):
        self.trees_chopped += 1

    def getTimesBanked(self):
        return self.times_banked

    def addTimesBanked(self):
        self.times_banked += 1

    def getLastTreeChopped(self):
        return self.last_tree_chopped

    def setLastTreeChopped(self, tree):
        self.last_tree_chopped = tree

    def randomTreeChooser(self):
        tree = None
        while tree is None:
            random_tree = random_tree = random.randint(1, 4)

            if random_tree == 1:
                for image in tree_1_maple_images:
                    tree = pyautogui.locateCenterOnScreen(image, confidence=0.75, grayscale=False, limit=3)

            elif random_tree == 2:
                for image in tree_2_maple_images:
                    tree = pyautogui.locateCenterOnScreen(image, confidence=0.75, grayscale=False, limit=3)
            elif random_tree == 3:
                for image in tree_2_maple_images:
                    tree = pyautogui.locateCenterOnScreen(image, confidence=0.75, grayscale=False, limit=3)
            else:
                for image in tree_2_maple_images:
                    tree = pyautogui.locateCenterOnScreen(image, confidence=0.75, grayscale=False, limit=3)
                # TODO tree 1 was chosen
            if tree is not None:
                print(f"tree {random_tree} was chosen")
                self.setLastTreeChopped(random_tree)
                return tree
            else:
                print(f"tree {random_tree} was not found")
                continue
