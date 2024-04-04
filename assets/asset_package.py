"""asset_package.py loads in image assets into array to be used"""
import os
import time


def get_root_path(image_array: list, folder: str) -> list:
    for index, image in enumerate(image_array):
        image_array[index] = folder + image
    return image_array


os.chdir("../.")  # sets chdir to root

try:
    # gets full path of images and puts them in array.
    tree_1_maple_images = get_root_path(os.listdir("assets/seers-village-maples/tree-1-maple/"),
                                        "assets/seers-village-maples/tree-1-maple/")

    tree_2_maple_images = get_root_path(os.listdir("assets/seers-village-maples/tree-2-maple/"),
                                        "assets/seers-village-maples/tree-2-maple/")

    tree_3_maple_images = get_root_path(os.listdir("assets/seers-village-maples/tree-3-maple/"),
                                        "assets/seers-village-maples/tree-3-maple/")

    tree_4_maple_images = get_root_path(os.listdir("assets/seers-village-maples/tree-4-maple/"),
                                        "assets/seers-village-maples/tree-4-maple/")

    maple_deposit = get_root_path(os.listdir("assets/seers-village-maples/maple-deposit/"),
                                  "assets/seers-village-maples/maple-deposit/")

    bank_images = get_root_path(os.listdir("assets/seers-village-maples/bank/"), "assets/seers-village-maples/bank/")

    tree_1_dead_maple = get_root_path(os.listdir("assets/seers-village-maples-dead/tree-1-maple/"),
                                      "assets/seers-village-maples-dead/tree-1-maple/")

    tree_2_dead_maple = get_root_path(os.listdir("assets/seers-village-maples-dead/tree-2-maple/"),
                                      "assets/seers-village-maples-dead/tree-2-maple/")

    tree_3_dead_maple = get_root_path(os.listdir("assets/seers-village-maples-dead/tree-3-maple/"),
                                      "assets/seers-village-maples-dead/tree-3-maple/")

    tree_4_dead_maple = get_root_path(os.listdir("assets/seers-village-maples-dead/tree-4-maple/"),
                                      "assets/seers-village-maples-dead/tree-4-maple/")

    compass_images = get_root_path(os.listdir("assets/compass/"), "assets/compass/")
except Exception as e:
    print("Error loading images, please check the assets folder and try again")
    print(e)
    time.sleep(2)
    quit()


def printAsiccArt() -> int:
    print(" __  __              _       _                      __     ___   ")
    print("|  \/  |  __ _    __| |   __| |    ___    __ __    /  \   | __|  ")
    print("| |\/| | / _` |  / _` |  / _` |   / _ \   \ \ /   | () |  |__ \  ")
    print("|_|__|_| \__,_|  \__,_|  \__,_|   \___/   /_\_\    \__/   |___/  ")
    print("By Maddox05 (https://github.com/maddox05)")
    return 0


if __name__ == "__main__":
    print("asset_package.py loads in image assets into array to be used.\nasset_package.py is not a standalone app")
