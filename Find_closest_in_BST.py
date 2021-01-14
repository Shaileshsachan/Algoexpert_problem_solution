# Average: O(log(n))  |  O(log(n))         (time     |    Space)
# Worst: O(n)   |   O(n)         ...if there is just a root node
def findClosestInBst(tree, target):
    return findClosestInBstHelper(tree, target, float("inf"))

def findClosestInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestInBstHelper(tree.right, target, closest)
    else:
        return closest


def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - tree.value):
            closest = tree.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode =  currentNode.right
        else:
            break
    return closest

