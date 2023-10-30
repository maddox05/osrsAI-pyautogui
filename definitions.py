# Description: Contains all the definitions for the bot, such as the image sets, and the functions that are used in
# the bot.
import time
import pyautogui


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
