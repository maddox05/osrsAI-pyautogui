import pyautogui
import random
import time
from pyclick import HumanClicker

from creator import BotCreator

"""
 * A Osrs bot made using pyautogui
 *
 * Made for Fun
 *
 * @author Maddox Schmidlkofer
 * @version September 17, 2023
"""

hc = HumanClicker() # init human clicker


def smooth_scroll(amount):
    """
    Smoothly scrolls the content by the specified amount.

    This function uses advanced pyautogui to provide a seamless scrolling experience,
    reducing jitters and ensuring a visually pleasing and user-friendly interface.

    Args:
        amount (int): The amount by which the content should be scrolled.
        * should be positive or negative, very case specific

    Returns:
        None
    """
    if amount == 5000:
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


def start():
    compass = pyautogui.locateCenterOnScreen("assets/compass.png", confidence=0.80, grayscale=False)
    if compass is not None:
        hc.move((compass.x, compass.y), random.uniform(.2, .8))
        pyautogui.click(button="left")
        hc.move((round(pyautogui.size().width / 2), round(pyautogui.size().height / 2)), random.uniform(.5, .8))
    else:
        print("could not find compass and cannot center direction to north")
        time.sleep(1)
    # type in username and password
    time.sleep(.4)
    smooth_scroll(5000)
    time.sleep(.3)
    smooth_scroll(-2500)
    time.sleep(.2)
    pyautogui.keyDown("up")
    time.sleep(random.randrange(3, 4))
    pyautogui.keyUp("up")


def reset():
    """
    Resets the player to the default position you picked.

    Scans screen and finds the reset button, then clicks it.

    Returns:
        Success if reset was successful,
        Quit if not successful
    """
    reset_spot = pyautogui.locateCenterOnScreen("assets/pink-reset.png", confidence=0.30, grayscale=False)
    if reset_spot is not None:
        hc.move((reset_spot.x, reset_spot.y),
                random.uniform(.2, .8))  # pyautogui.moveTo(reset_spot.x, reset_spot.y, duration=1)
        pyautogui.click(button="left")
        time.sleep(random.randint(3, 5))
        print("reset successful")
        return "Success"
    else:
        print("could not reset, ending now")
        time.sleep(1)
        #return "Failed"
        quit()


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
    bank = pyautogui.locateCenterOnScreen("assets/seers-village-maples/bank-seers.png", confidence=0.85,
                                          grayscale=False)
    if bank is not None:  # may need to type bank code
        try:
            hc.move((bank.x, bank.y), random.uniform(.5, .8))
            pyautogui.click(button="left")
            time.sleep(random.uniform(11, 12))
            log = locateLog()
            hc.move((log.x, log.y), random.uniform(.5, .8))
            pyautogui.click(button="right")
            deposit_button = pyautogui.locateCenterOnScreen("assets/seers-village-maples/deposit-all-maple-logs.png",
                                                            confidence=0.70,
                                                            grayscale=False,
                                                            limit=3)
            hc.move((deposit_button.x, deposit_button.y),
                    random.uniform(.2, .8))  # deposit chooses 10 instead of 50 or all
            pyautogui.click(button="left")
            pyautogui.keyDown("esc")
            time.sleep(.05)
            pyautogui.keyUp("esc")
            time.sleep(.2)
            print("banked successfully")

        except:
            print("failed to bank, fatal error")
            time.sleep(2)
            quit()

    else:
        print("failed to bank, fatal error")
        time.sleep(1)
        quit()


def chopTreesMaplesSeers():
    """
    Recursive loop that chops trees, banks, and repeats

    This function should be called after the player has logged in and is ready to chop trees.

    Returns:
        None (it is recursive)
    """
    # reset()
    tree = main_bot.randomTreeChooser()  # fix later but call with certain instance of bot
    if tree is not None:
        hc.move((tree.x, tree.y), random.uniform(.2, .8))  # pyautogui.moveTo(tree.x, tree.y, duration=1)
        pyautogui.click(button="left")
        time.sleep(random.randint(4, 5))

        if didSwing() and amountOfMapleLogs() < 26:
            print("chopping now!")
            time.sleep(random.randint(65, 70))  # should add something to check if tree is finished chopping
            if reset() == "Success":
                main_bot.addTreeChopped()
                chopTreesMaplesSeers()
            else:
                print("could not reset fatal error")
                time.sleep(1)
                quit()
        else:
            if reset() == "Success":
                bankAtSeers()
                if reset() == "Success":
                    print("sleeping for 10 seconds")
                    time.sleep(random.uniform(9, 11))

                    chopTreesMaplesSeers()
                else:
                    print("could not reset, fatal error")
                    time.sleep(2)
                    quit()
    else:
        print("No trees available.\nfatal error")
        time.sleep(1)
        quit()


if __name__ == "__main__":
    main_bot = BotCreator("Seers_Village", "bot", "1234", "1234")
    time.sleep(2)
    start()
    chopTreesMaplesSeers()
