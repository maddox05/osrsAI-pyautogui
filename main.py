try:
    import os
    import pyautogui
    import PIL
    import random
    import time
    from pyclick import HumanClicker
    import pyscreeze

    from creator import BotCreator, MapleCutter
    from assets import *

    screen_size = pyautogui.size()
    screen_size_multiplier = 1
    time.sleep(.1)
    print(f"your screen size is {screen_size} if this is incorrect than open an issue on github.")
    # for macOS version of PIL
    if os.getenv("HOME"):  # in mac and linux but not in windows
        yes_or_no = input(
            "would you like to double screen size? (MACOS retina fix) y or n\n")  # remove when macOS is supported
        if yes_or_no == "y":
            screen_size_multiplier = 2
            screen_size = (screen_size[0] * 2, screen_size[1] * 2)
            print(f"your New screen size is {screen_size} if this is incorrect than open an issue on github.")
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


def start():  # When instances of bot are created added to this program, this function will be called every time a
    # new bot is created and started

    """
        Starts up the script and gets the program ready to run.
        Returns:
            None
    """
    printAsiccArt()
    time.sleep(.1)
    print("Starting bot")

    compass = None
    compass = loopImages(compass_images, limit=3, confidence=0.75, grayscale=False)
    if compass is not None:
        hc.move((round(compass.x / screen_size_multiplier), round(compass.y / screen_size_multiplier)),
                random.uniform(.2, .8))
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


if __name__ == "__main__":
    maple_bot = MapleCutter("Seers_Village", "bot", "1234", "1234")
    time.sleep(2)
    start()
    maple_bot.chopTreesMaplesSeers()
