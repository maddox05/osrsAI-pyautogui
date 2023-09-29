from main import *


class BotCreator:
    """
    Used to create different instances of the bot, not fully implemented yet
    """
    # fires_made = 0
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


class MapleCutter(BotCreator):
    """
    Maple Tree Cutting bot, inherits from BotCreator
    """

    trees_chopped = 0
    last_tree_chopped = 0

    def __init__(self, location, username, password, bank_pin):
        super().__init__(location, username, password, bank_pin)

    def randomTreeChooser(self):
        """
        Chooses a random tree on the screen and returns it.

        Loops until a tree is found.

        Returns:
            the tree object that was chosen
        """
        times_looped = 0
        tree = None
        while tree is None:
            if times_looped >= 10:
                print("failed to find trees after 10 tries, resetting")
                if self.reset() == "Success":
                    self.chopTreesMaplesSeers()
                else:
                    print(FATAL_ERROR)
                    time.sleep(2)
                    stopBot()
            random_tree = random.randint(1, 4)

            if random_tree == 1:
                tree = loopImages(tree_1_maple_images, limit=1, confidence=0.75, grayscale=False)

            elif random_tree == 2:
                tree = loopImages(tree_2_maple_images, limit=1, confidence=0.75, grayscale=False)

            elif random_tree == 3:
                tree = loopImages(tree_3_maple_images, limit=1, confidence=0.75, grayscale=False)

            else:
                tree = loopImages(tree_4_maple_images, limit=1, confidence=0.75, grayscale=False)
            if tree is not None:
                print(f"tree {random_tree} was chosen")
                self.setLastTreeChopped(random_tree)
                return tree
            else:
                print(f"tree {random_tree} was not found")
                times_looped += 1
                continue

    def reset(self):
        """
        Resets the player to the default position you picked.

        Scans screen and finds the reset button, then clicks it.

        Returns:
            Success if reset was successful,
            Quit if not successful
        """
        reset_spot = pyautogui.locateCenterOnScreen("assets/pink-reset.png", confidence=0.30, grayscale=False, limit=2)
        if reset_spot is not None:
            hc.move((round(reset_spot.x / screen_size_multiplier), round(reset_spot.y / screen_size_multiplier)),
                    random.uniform(.2, .8))  # pyautogui.moveTo(reset_spot.x, reset_spot.y, duration=1)
            pyautogui.click(button="left")
            time.sleep(random.randint(3, 5))
            print("reset successful")
            return "Success"
        else:
            print(FATAL_ERROR)
            time.sleep(1)
            stopBot()

    def isInventoryFull(self):
        """
        Checks if the inventory is full by checking if message has been sent that inventory is full.
        Returns:
            True if inventory is full //
            False if inventory is not full
        """
        full = pyautogui.locateOnScreen("assets/seers-village-maples/inventory-full-maple-new.png", confidence=0.80,
                                        grayscale=False)
        if full is None:
            return True
        else:
            return False

    def currentAmountOfLogs(self):
        """
        Checks how many maple logs are in the inventory

        Returns:
            Amount of maple logs in inventory
        """
        amt_logs = 0
        logs = pyautogui.locateAllOnScreen("assets/seers-village-maples/maple-log.png", confidence=0.982,
                                           grayscale=False)
        for _ in logs:
            amt_logs += 1
        print(f"amount of maple logs: {amt_logs}")
        return amt_logs

    def locateLog(self):
        """
        Locates log (for banking)

        Returns:
            log (pyautogui.Point): The location of the log
        """
        log = pyautogui.locateCenterOnScreen("assets/seers-village-maples/maple-log.png", confidence=0.85,
                                             grayscale=False)
        if log is not None:
            return log

    def bank(self):
        """
        Banks at seers village

        Finds bank, clicks it, deposits all logs, and closes bank


        Returns:
            None
        """
        bank = None
        for bank_image in bank_images:
            bank = pyautogui.locateCenterOnScreen(bank_image, confidence=0.85,
                                                  grayscale=False, limit=2)
            if bank is not None:
                break

        if bank is not None:  # may need to type bank code
            try:
                hc.move((round(bank.x / screen_size_multiplier), round(bank.y / screen_size_multiplier)),
                        random.uniform(.5, .8))
                pyautogui.click(button="left")
                time.sleep(random.uniform(11, 12))
                log = self.locateLog()
                hc.move((round(log.x / screen_size_multiplier), round(log.y / screen_size_multiplier)),
                        random.uniform(.5, .8))
                pyautogui.click(button="right")
                deposit_button = loopImages(maple_deposit, limit=3, confidence=0.75, grayscale=False)
                if deposit_button is None:
                    print("could not find deposit button, fatal error")
                    time.sleep(1)
                    stopBot()
                hc.move((round(deposit_button.x / screen_size_multiplier),
                         round(deposit_button.y / screen_size_multiplier)),
                        random.uniform(.2, .8))  # deposit chooses 10 instead of 50 or all
                pyautogui.click(button="left")
                pyautogui.keyDown("esc")
                time.sleep(.05)
                pyautogui.keyUp("esc")
                time.sleep(.2)
                print("banked successfully")

            except:
                print("failed to bank")
                print(FATAL_ERROR)
                time.sleep(2)
                stopBot()

        else:
            print("failed to bank")
            print(FATAL_ERROR)
            time.sleep(1)
            stopBot()

    def isTreeBroken(self, current_tree) -> bool:
        """
        Checks if the tree is broken
        Args:
            current_tree:

        Returns:
            True or False depending on if the current tree is broken

        """
        tree = None
        if current_tree == 1:
            for image in tree_1_dead_maple:
                tree = pyautogui.locateCenterOnScreen(image, confidence=0.90, grayscale=False, limit=1)
                if tree is not None:
                    print(f"tree {self.getLastTreeChopped()} is broken")
                    return True
        elif current_tree == 2:
            for image in tree_2_dead_maple:
                tree = pyautogui.locateCenterOnScreen(image, confidence=0.90, grayscale=False, limit=1)
                if tree is not None:
                    print(f"tree {self.getLastTreeChopped()} is broken")
                    return True
        elif current_tree == 3:
            for image in tree_2_dead_maple:
                tree = pyautogui.locateCenterOnScreen(image, confidence=0.90, grayscale=False, limit=1)
                if tree is not None:
                    print(f"tree {self.getLastTreeChopped()} is broken")
                    return True
        else:
            for image in tree_2_dead_maple:
                tree = pyautogui.locateCenterOnScreen(image, confidence=0.90, grayscale=False, limit=1)
                if tree is not None:
                    print(f"tree {self.getLastTreeChopped()} is broken")
                    return True
        if tree is not None:
            print(f"tree {self.getLastTreeChopped()} is broken")
            return True
        else:
            print(f"tree {self.getLastTreeChopped()} is NOT broken")
            return False

    def chopTreesMaplesSeers(self):
        """
        Recursive loop that chops trees, banks, and repeats

        This function should be called after the player has logged in and is ready to chop trees.

        Returns:
            None (it is recursive)
        """
        # reset()
        if self.currentAmountOfLogs() < 24:
            tree = self.randomTreeChooser()  # fix later but call with certain instance of bot

            if tree is not None:
                hc.move((round(tree.x / screen_size_multiplier), round(tree.y / screen_size_multiplier)),
                        random.uniform(.2, .8))  # pyautogui.moveTo(tree.x, tree.y, duration=1)
                pyautogui.click(button="left")
                time.sleep(random.randint(4, 5))

                time.sleep(random.randint(36, 38))  # does not work well if other players
                for i in range(0, 60):
                    if self.isTreeBroken(self.getLastTreeChopped()):
                        break
                    else:
                        time.sleep(random.uniform(5, 7))
                # if reset() == "Success":
                self.addTreeChopped()
                self.chopTreesMaplesSeers()
            else:
                print("No trees available.")
                print(FATAL_ERROR)
                time.sleep(1)
                stopBot()

        else:
            if self.reset() == "Success":  # reset
                self.bank()  # bank
                if self.reset() == "Success":  # after banking reset
                    print("sleeping for 10 seconds")  # let bro walk to reset spot
                    time.sleep(random.uniform(9, 11))
                    self.chopTreesMaplesSeers()  # call it again
                else:  # should never happen as reset quits when it fails
                    print("could not reset")
                    print(FATAL_ERROR)
                    time.sleep(2)
                    stopBot()
