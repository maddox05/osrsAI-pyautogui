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
    reset_spot = pyautogui.locateCenterOnScreen("assets/pink-reset.png", confidence=0.30, grayscale=False)
    if reset_spot is not None:
        hc.move((reset_spot.x, reset_spot.y),
                random.uniform(.5, .8))  # pyautogui.moveTo(reset_spot.x, reset_spot.y, duration=1)
        pyautogui.click(button="left")
        time.sleep(random.randint(3, 5))
        print("reset successful")
        return "Success"
    else:
        print("could not reset, ending now")
        quit()


def isInventoryFull():
    full = pyautogui.locateOnScreen("assets/seers-village-maples/inventory-full-maple-new.png", confidence=0.80,
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


def amountOfMapleLogs():
    amt_logs = 0
    logs = pyautogui.locateAllOnScreen("assets/seers-village-maples/maple-log.png", confidence=0.982, grayscale=False)
    for _ in logs:
        amt_logs += 1
    print(f"amount of maple logs: {amt_logs}")
    return amt_logs


def locateLog():
    log = pyautogui.locateCenterOnScreen("assets/seers-village-maples/maple-log.png", confidence=0.85, grayscale=False)
    if log is not None:
        return log


def bankAtSeers():
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
                                                            confidence=0.65,
                                                            grayscale=False,
                                                            limit=2)
            hc.move((deposit_button.x, deposit_button.y), random.uniform(.5, .8))
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
    # reset()
    tree = randomTreeChooser()
    if tree is not None:
        hc.move((tree.x, tree.y), random.uniform(.5, .8))  # pyautogui.moveTo(tree.x, tree.y, duration=1)
        pyautogui.click(button="left")
        time.sleep(random.randint(4, 5))

        if didSwing() and amountOfMapleLogs() < 23:
            print("chopping now!")
            time.sleep(random.randint(62, 68))  # should add something to check if tree is finished chopping
            if reset() == "Success":
                main_bot.addTreeChopped()
                chopTreesMaplesSeers()
            else:
                print("could not reset fatal error")
                quit()
        else:
            if isInventoryFull():  # won't work 100% of time as if message exist anywhere it will fire
                print("inventory is full")
                if amountOfMapleLogs() >= 23:
                    if reset() == "Success":
                        bankAtSeers()
                        if reset() == "Success":
                            chopTreesMaplesSeers()
                        else:
                            print("could not reset, fatal error")
                            time.sleep(2)
                            quit()

            else:
                if amountOfMapleLogs() >= 23:
                    if reset() == "Success":
                        bankAtSeers()
                        reset()
                        time.sleep(random.uniform(9, 11))
                        chopTreesMaplesSeers()
    else:
        print("No trees available.\nfatal error")
        time.sleep(1)
        quit()


def randomTreeChooser():
    tree = None
    while tree is None:
        random_tree = random.randint(1, 4)
        if random_tree == 1:
            tree = pyautogui.locateCenterOnScreen("assets/seers-village-maples/tree-maple-1st.png", confidence=0.70,
                                                  grayscale=False)
        if random_tree == 2:
            tree = pyautogui.locateCenterOnScreen("assets/seers-village-maples/tree-maple-2nd.png", confidence=0.70,
                                                  grayscale=False)
        if random_tree == 3:
            tree = pyautogui.locateCenterOnScreen("assets/seers-village-maples/tree-maple-3rd.png", confidence=0.80,
                                                  grayscale=False)
        else:
            tree = pyautogui.locateCenterOnScreen("assets/seers-village-maples/tree-maple-4th.png", confidence=0.70,
                                                  grayscale=False)
        if tree is not None:
            print(f"tree {random_tree} was chosen")
            return tree


if __name__ == "__main__":
    main_bot = BotCreator("Seers_Village", "bot", "1234")
    time.sleep(2)
    start()
    chopTreesMaplesSeers()
