import node as n

count = 0
root = True

def addNode(pos, n):
    if n == None:
        pos = n
    else:
        if pos.value < n.value:
            if pos.right == None:
                pos.right = n
            else:
                addNode(pos.right, n)
        else:
            if pos.left == None:
                pos.left = n
            else:
                addNode(pos.left, n)

def countNodes(n):
    if n != None:
        countNodes(n.left)
        global count
        count+=1
        countNodes(n.right)
    return count

def treeHeight(n):
    if n == None:
        return -1
    else:
        return (1+max(treeHeight(n.left), treeHeight(n.right)))

def printTree(n):
    if n.left is not None:
        printTree(n.left)
    print(n.value())
    if n.right is not None:
        printTree(n.right)

def printBranches(n, arr):
    word = '{}{}'.format(arr, n.letter)
    # si es hoja
    if n.left is None and n.right is None:
        print(word)           
    else:
        if n.left is not None:
            printBranches(n.left, word)
        if n.right is not None:
            printBranches(n.right, word)

#Generar arboles
tree = n.Node(4)
addNode(tree, n.Node(1))
addNode(tree, n.Node(2))
addNode(tree, n.Node(3))
addNode(tree, n.Node(5))
addNode(tree, n.Node(6))
addNode(tree, n.Node(7))
addNode(tree, n.Node(8))

treeString = n.NodeString("B", 12)
addNode(treeString, n.NodeString("U", 6))
addNode(treeString, n.NodeString("E", 5))
addNode(treeString, n.NodeString("N", 2))
addNode(treeString, n.NodeString("O", 1))
addNode(treeString, n.NodeString("A", 3))
addNode(treeString, n.NodeString("S", 4))
addNode(treeString, n.NodeString("R", 7))
addNode(treeString, n.NodeString("R", 9))
addNode(treeString, n.NodeString("A", 8))
addNode(treeString, n.NodeString("O", 11))
addNode(treeString, n.NodeString("S", 10))
addNode(treeString, n.NodeString("I", 15))
addNode(treeString, n.NodeString("E", 14))
addNode(treeString, n.NodeString("N", 13))
addNode(treeString, n.NodeString("L", 19))
addNode(treeString, n.NodeString("B", 18))
addNode(treeString, n.NodeString("A", 17))
addNode(treeString, n.NodeString("O", 16))