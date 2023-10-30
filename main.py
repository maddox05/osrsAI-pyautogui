from mapletree import MapleCutter
from definitions import *

try:
    import os
    import pyautogui
    import PIL
    import random
    import time
    from pyclick import HumanClicker
    import pyscreeze

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



# Constants
FATAL_ERROR = "FATAL ERROR, QUITTING NOW"

try:
    hc = HumanClicker()  # init human clicker
except:
    print("Failed to initialize human clicker (open a issue on github)")
    print(FATAL_ERROR)
    time.sleep(5)
    quit()


def start():  # When instances of bot are created added to this program, this function will be called every time a bot is created
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

"""
 * A OSRS AI bot made using pyautogui
 *
 * Made for Fun
 *
 * @author Maddox Schmidlkofer
 * @version September 17, 2023
"""
if __name__ == "__main__":
    maple_bot = MapleCutter("Seers_Village", "bot", "1234", "1234")  # look at later import creator
    time.sleep(2)
    start() #maple_bot.start()
    maple_bot.chopTreesMaplesSeers()
