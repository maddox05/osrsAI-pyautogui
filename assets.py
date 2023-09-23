import os


def getFullPath(image_array, folder) -> list:
    for index, image in enumerate(image_array):

        image_array[index] = folder + image
    return image_array


tree_1_maple_images = os.listdir("assets/seers-village-maples/tree-1-maple/")
tree_1_maple_images = getFullPath(tree_1_maple_images, "assets/seers-village-maples/tree-1-maple/")

tree_2_maple_images = os.listdir("assets/seers-village-maples/tree-2-maple/")
tree_2_maple_images = getFullPath(tree_2_maple_images, "assets/seers-village-maples/tree-2-maple/")

tree_3_maple_images = os.listdir("assets/seers-village-maples/tree-3-maple/")
tree_3_maple_images = getFullPath(tree_3_maple_images, "assets/seers-village-maples/tree-3-maple/")

tree_4_maple_images = os.listdir("assets/seers-village-maples/tree-4-maple/")
tree_4_maple_images = getFullPath(tree_4_maple_images, "assets/seers-village-maples/tree-4-maple/")

maple_deposit = os.listdir("assets/seers-village-maples/maple-deposit/")
maple_deposit = getFullPath(maple_deposit, "assets/seers-village-maples/maple-deposit/")

bank_images = os.listdir("assets/seers-village-maples/bank/")
bank_images = getFullPath(bank_images, "assets/seers-village-maples/bank/")

tree_1_dead_maple = os.listdir("assets/seers-village-maples-dead/tree-1-maple/")
tree_1_dead_maple = getFullPath(tree_1_dead_maple, "assets/seers-village-maples-dead/tree-1-maple/")

tree_2_dead_maple = os.listdir("assets/seers-village-maples-dead/tree-2-maple/")
tree_2_dead_maple = getFullPath(tree_2_dead_maple, "assets/seers-village-maples-dead/tree-2-maple/")

tree_3_dead_maple = os.listdir("assets/seers-village-maples-dead/tree-3-maple/")
tree_3_dead_maple = getFullPath(tree_3_dead_maple, "assets/seers-village-maples-dead/tree-3-maple/")

tree_4_dead_maple = os.listdir("assets/seers-village-maples-dead/tree-4-maple/")
tree_4_dead_maple = getFullPath(tree_4_dead_maple, "assets/seers-village-maples-dead/tree-4-maple/")

compass_images = os.listdir("assets/compass/")
compass_images = getFullPath(compass_images, "assets/compass/")


def printAsiccArt():
    print(" __  __              _       _                      __     ___   ")
    print("|  \/  |  __ _    __| |   __| |    ___    __ __    /  \   | __|  ")
    print("| |\/| | / _` |  / _` |  / _` |   / _ \   \ \ /   | () |  |__ \  ")
    print("|_|__|_| \__,_|  \__,_|  \__,_|   \___/   /_\_\   _\__/   |___/  ")
    print("By Maddox05 (https://github.com/maddox05)")
