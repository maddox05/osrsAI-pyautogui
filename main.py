try:
    import os
    import pyautogui
    import PIL
    import random
    import time
    from pyclick import HumanClicker
    import pyscreeze

    from creator import BotCreator
    from assets import *

    # for macOS version of PIL
    if os.getenv("HOME"):  # in mac and linux but not in windows
        print("MacOS is not supported yet, quitting now")  # remove when macOS is supoorted
        time.sleep(1.5)
        quit()
        # mac cant read images as they have improper permissions
        __PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
        pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION
    else:
        print("Windows detected")

    ##############################
except ImportError as e:
    # Log the specific error message and traceback
    import logging

    logging.error(f"Failed to import a module: {e}")
    raise  # Re-raise the exception for further diagnosis

"""
 * A OSRS AI bot made using pyautogui
 *
 * Made for Fun
 *
 * @author Maddox Schmidlkofer
 * @version September 17, 2023
"""

# Constants
FATAL_ERROR = "FATAL ERROR, QUITTING NOW"

try:
    hc = HumanClicker()  # init human clicker
except:
    print("Failed to initialize human clicker (open a issue on github)")
    print(FATAL_ERROR)
    time.sleep(5)
    quit()

def stopBot():
    """
    Stops the bot and quits the program.

    Returns:
        None
    """
    print("Stopping bot")
    time.sleep(1)
    quit()


def loopImages(image_set, limit, confidence, grayscale):
    """
    Loops through the images in the assets folder and prints them to the console.

    Returns:
        Image object that is found on screen // can return none if no image is found
    """
    return_image = None
    for image in image_set:
        return_image = pyautogui.locateCenterOnScreen(image, confidence=confidence, grayscale=grayscale, limit=limit)
        if return_image is not None:
            break
    return return_image


def smooth_scroll(amount):
    """
    Smoothly scrolls the content by the specified amount.

    This function advances pyautogui scroll function to provide a seamless scrolling experience,
    reducing jitters and ensuring a visually pleasing and user-friendly experience.

    Args:
        amount (int): The amount by which the content should be scrolled. Same amount as used in pyautogui will be scrolled, but the scrolling will be smoother.
        * should be positive or negative, very case specific

    Returns:
        None
    """
    if amount == 5000:  # scrolls different depending on windows or macOS # make python lib with this use math though
        pyautogui.scroll(clicks=500)
        pyautogui.scroll(clicks=500)
        pyautogui.scroll(clicks=500)
        pyautogui.scroll(clicks=500)
        pyautogui.scroll(clicks=500)
        pyautogui.scroll(clicks=500)
        pyautogui.scroll(clicks=500)
        pyautogui.scroll(clicks=500)
        pyautogui.scroll(clicks=500)
        pyautogui.scroll(clicks=500)
    else:
        pyautogui.scroll(clicks=-500)
        pyautogui.scroll(clicks=-500)
        pyautogui.scroll(clicks=-500)
        pyautogui.scroll(clicks=-500)
        pyautogui.scroll(clicks=-500)


def start():  # When instances of bot are created added to this program, this function will be called every time a new bot is created

    """
        Starts up the script and gets the user ready to chop trees.
        Returns:
            None
    """
    printAsiccArt()
    time.sleep(.1)
    print("Starting bot")
    screen_size = pyautogui.size()
    time.sleep(.1)
    print(f"your screen size is {screen_size} if this is incorrect than open an issue on github.")
    time.sleep(1)
    compass = None
    compass = loopImages(compass_images, limit=3, confidence=0.75, grayscale=False)
    if compass is not None:
        hc.move((compass.x, compass.y), random.uniform(.2, .8))
        pyautogui.click(button="left")
        hc.move((round(pyautogui.size().width / 2), round(pyautogui.size().height / 2)), random.uniform(.5, .8))
    else:
        print("could not find compass and cannot center direction to north")
        print(FATAL_ERROR)
        time.sleep(2)
        stopBot()
    # type in username and password
    time.sleep(.4)
    smooth_scroll(5000)
    time.sleep(.3)
    smooth_scroll(-2500)
    time.sleep(.2)
    pyautogui.keyDown("up")
    time.sleep(random.randrange(3, 4))
    pyautogui.keyUp("up")


def randomTreeChooser():
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
            if reset() == "Success":
                chopTreesMaplesSeers()
            else:
                print(FATAL_ERROR)
                time.sleep(2)
                stopBot()
        random_tree = random_tree = random.randint(1, 4)

        if random_tree == 1:
            tree = loopImages(tree_1_maple_images, limit=2, confidence=0.75, grayscale=False)

        elif random_tree == 2:
            tree = loopImages(tree_2_maple_images, limit=2, confidence=0.75, grayscale=False)

        elif random_tree == 3:
            tree = loopImages(tree_3_maple_images, limit=2, confidence=0.75, grayscale=False)

        else:
            tree = loopImages(tree_4_maple_images, limit=2, confidence=0.75, grayscale=False)
        if tree is not None:
            print(f"tree {random_tree} was chosen")
            main_bot.setLastTreeChopped(random_tree)
            return tree
        else:
            print(f"tree {random_tree} was not found")
            times_looped += 1
            continue


def reset():
    """
    Resets the player to the default position you picked.

    Scans screen and finds the reset button, then clicks it.

    Returns:
        Success if reset was successful,
        Quit if not successful
    """
    reset_spot = pyautogui.locateCenterOnScreen("assets/pink-reset.png", confidence=0.30, grayscale=False, limit=2)
    if reset_spot is not None:
        hc.move((reset_spot.x, reset_spot.y),
                random.uniform(.2, .8))  # pyautogui.moveTo(reset_spot.x, reset_spot.y, duration=1)
        pyautogui.click(button="left")
        time.sleep(random.randint(3, 5))
        print("reset successful")
        return "Success"
    else:
        print(FATAL_ERROR)
        time.sleep(1)
        stopBot()


def isInventoryFull():
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


def didSwing():
    """
    Checks if the player has swung the axe yet,
     using the message box, prone to error as multiple messages don't get deleted,
    so may check old messages
    Returns:
        True if player has swung axe //
        False if player has not swung axe
    """
    did_swing = pyautogui.locateOnScreen("assets/seers-village-maples/u-swing-axe.png", confidence=0.90,
                                         grayscale=False)
    if did_swing is not None:
        return True
    else:
        return False


def amountOfMapleLogs():
    """
    Checks how many maple logs are in the inventory

    Returns:
        Amount of maple logs in inventory
    """
    amt_logs = 0
    logs = pyautogui.locateAllOnScreen("assets/seers-village-maples/maple-log.png", confidence=0.982, grayscale=False)
    for _ in logs:
        amt_logs += 1
    print(f"amount of maple logs: {amt_logs}")
    return amt_logs


def locateLog():
    """
    Locates log (for banking)

    Returns:
        log (pyautogui.Point): The location of the log
    """
    log = pyautogui.locateCenterOnScreen("assets/seers-village-maples/maple-log.png", confidence=0.85, grayscale=False)
    if log is not None:
        return log


def bankAtSeers():
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
            hc.move((bank.x, bank.y), random.uniform(.5, .8))
            pyautogui.click(button="left")
            time.sleep(random.uniform(11, 12))
            log = locateLog()
            hc.move((log.x, log.y), random.uniform(.5, .8))
            pyautogui.click(button="right")
            deposit_button = loopImages(maple_deposit, limit=3, confidence=0.75, grayscale=False)
            if deposit_button is None:
                print("could not find deposit button, fatal error")
                time.sleep(1)
                stopBot()
            hc.move((deposit_button.x, deposit_button.y),
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


def isTreeBroken(current_tree):  # TODO: fix this
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
                print(f"tree {main_bot.getLastTreeChopped()} is broken")
                return True
    elif current_tree == 2:
        for image in tree_2_dead_maple:
            tree = pyautogui.locateCenterOnScreen(image, confidence=0.90, grayscale=False, limit=1)
            if tree is not None:
                print(f"tree {main_bot.getLastTreeChopped()} is broken")
                return True
    elif current_tree == 3:
        for image in tree_2_dead_maple:
            tree = pyautogui.locateCenterOnScreen(image, confidence=0.90, grayscale=False, limit=1)
            if tree is not None:
                print(f"tree {main_bot.getLastTreeChopped()} is broken")
                return True
    else:
        for image in tree_2_dead_maple:
            tree = pyautogui.locateCenterOnScreen(image, confidence=0.90, grayscale=False, limit=1)
            if tree is not None:
                print(f"tree {main_bot.getLastTreeChopped()} is broken")
                return True
    if tree is not None:
        print(f"tree {main_bot.getLastTreeChopped()} is broken")
        return True
    else:
        print(f"tree {main_bot.getLastTreeChopped()} is NOT broken")
        return False


def chopTreesMaplesSeers():
    """
    Recursive loop that chops trees, banks, and repeats

    This function should be called after the player has logged in and is ready to chop trees.

    Returns:
        None (it is recursive)
    """
    # reset()
    tree = randomTreeChooser()  # fix later but call with certain instance of bot
    if tree is not None:
        hc.move((tree.x, tree.y), random.uniform(.2, .8))  # pyautogui.moveTo(tree.x, tree.y, duration=1)
        pyautogui.click(button="left")
        time.sleep(random.randint(4, 5))

        if amountOfMapleLogs() < 23:
            print("chopping now!")

            time.sleep(random.randint(36, 38))  # does not work well if other players
            for i in range(0, 60):
                if isTreeBroken(main_bot.getLastTreeChopped()):
                    break
                else:
                    time.sleep(random.uniform(5, 7))
            #if reset() == "Success":
            main_bot.addTreeChopped()
            chopTreesMaplesSeers()

        else:
            if reset() == "Success":  # reset
                bankAtSeers()  # bank
                if reset() == "Success":  # after banking reset
                    print("sleeping for 10 seconds")  # let bro walk to reset spot
                    time.sleep(random.uniform(9, 11))
                    chopTreesMaplesSeers()  # call it again
                else:  # should never happen as reset quits when it fails
                    print("could not reset")
                    print(FATAL_ERROR)
                    time.sleep(2)
                    stopBot()
    else:
        print("No trees available.")
        print(FATAL_ERROR)
        time.sleep(1)
        stopBot()


if __name__ == "__main__":
    main_bot = BotCreator("Seers_Village", "bot", "1234", "1234")
    time.sleep(2)
    start()
    chopTreesMaplesSeers()
