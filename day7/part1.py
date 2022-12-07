arr = []
with open('day7/input.txt', 'r') as f:
    arr = f.read().splitlines()

class Node():
    parent = None
    children = {}
    items = {}

    def __init__(self, parent, children, items):
        self.parent = parent
        self.children = children
        self.items = items

root = curr_node = None

# construct file tree
for i in range(len(arr)):
    line = arr[i]
    if line.startswith('$'):
        c = line.split(' ')
        if c[1] == 'cd':
            if curr_node:
                if c[2] == '..':
                    curr_node = curr_node.parent
                else:
                    parent = curr_node
                    curr_node = curr_node.children[c[2]]
            else:
                curr_node = Node(None, {}, {})
                root = curr_node

        elif c[1] == 'ls':
            n = i+1
            while n < len(arr) and arr[n][0] != '$':
                l,r = arr[n].split(' ')
                if l == 'dir':
                    curr_node.children[r] = Node(curr_node, {}, {})
                else:
                    curr_node.items[r] = int(l)
                n += 1
    else:
        continue


result = 0

# recursively traverse tree and calculate size of each directory
def getSize(node):
    global result
    children_size = 0

    for child in node.children:
        children_size += getSize(node.children[child])

    total_size = children_size + sum(node.items.values())

    if total_size < 100000:
        result += total_size

    return total_size

getSize(root)

print(result)