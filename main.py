import pyautogui
import random
import time
from pyclick import HumanClicker

from creator import BotCreator

hc = HumanClicker()


def smooth_scroll(amount):
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
        hc.move((compass.x, compass.y), random.uniform(.5, .8))
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
    reset_spot = pyautogui.locateCenterOnScreen("assets/pink-reset.png", confidence=0.50, grayscale=False)
    if reset_spot is not None:
        hc.move((reset_spot.x, reset_spot.y),
                random.uniform(.5, .8))  # pyautogui.moveTo(reset_spot.x, reset_spot.y, duration=1)
        pyautogui.click(button="left")
        time.sleep(random.randint(3, 5))
        return "Success"
    else:
        print("could not reset, ending now")
        quit()


def isInventoryFull():
    full = pyautogui.locateCenterOnScreen("assets/seers-village-maple/inventory-full-maple.png", confidence=0.80,
                                          grayscale=False)
    if full is None:
        return True
    else:
        return False


def didSwing():
    did_swing = pyautogui.locateOnScreen("assets/seers-village-maples/u-swing-axe.png", confidence=0.90,
                                         grayscale=False)
    if did_swing is not None:
        return True
    else:
        return False


def chopTreesMaplesSeers():
    tree = randomTreeChooser()
    if tree is not None:
        hc.move((tree.x, tree.y), random.uniform(.5, .8))  # pyautogui.moveTo(tree.x, tree.y, duration=1)
        pyautogui.click(button="left")
        time.sleep(random.randint(4, 5))

        if didSwing():
            time.sleep(random.randint(58, 64))
            if reset() == "Success":
                main_bot.addTreeChopped()
                chopTreesMaplesSeers()
            else:
                print("could not reset fatal error")
                quit()
        else:
            if isInventoryFull():
                print("inventory is full")
            else:
                print("tree hit failed")

            # reset
    else:
        print("No trees available.\n trying again")
        chopTreesMaplesSeers()
    # 20 scrolls


def randomTreeChooser():
    random_tree = random.randint(1, 4)
    if random_tree == 1:
        tree = pyautogui.locateCenterOnScreen("assets/seers-village-maples/tree-maple-1st.png", confidence=0.80,
                                              grayscale=False)
    if random_tree == 2:
        tree = pyautogui.locateCenterOnScreen("assets/seers-village-maples/tree-maple-2nd.png", confidence=0.80,
                                              grayscale=False)
    if random_tree == 3:
        tree = pyautogui.locateCenterOnScreen("assets/seers-village-maples/tree-maple-3rd.png", confidence=0.80,
                                              grayscale=False)
    else:
        tree = pyautogui.locateCenterOnScreen("assets/seers-village-maples/tree-maple-4th.png", confidence=0.80,
                                              grayscale=False)
    if tree is None:
        return tree
    else:
        print(f"tree {random_tree} was chosen")
        return tree


if __name__ == "__main__":
    main_bot = BotCreator("Seers_Village", "bot", "1234")
    time.sleep(2)
    start()
    chopTreesMaplesSeers()
