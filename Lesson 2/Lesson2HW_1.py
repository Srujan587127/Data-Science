class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        self.left = None
        self.right = None

def insert(root, roll, name):
    if root == None:
        return Student(roll, name)
    if roll < root.roll:
        root.left = insert(root.left, roll, name)
    else:
        root.right = insert(root.right, roll, name)
    return root

def search(root, roll):
    if root == None or root.roll == roll:
        return root
    if roll < root.roll:
        return search(root.left, roll)
    return search(root.right, roll)

def inorder(root, lst):
    if root:
        inorder(root.left, lst)
        lst.append(root)
        inorder(root.right, lst)
    return lst

def binary_search(lst, roll):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid].roll == roll:
            return lst[mid]
        if lst[mid].roll < roll:
            low = mid + 1
        else:
            high = mid - 1
    return None

school = {"Gate": ["Office"], "Office": ["Gate", "Library", "Class A"], "Library": ["Office"], "Class A": ["Office", "Lab"], "Lab": ["Class A"], "Gym": []}

def bfs(start, end):
    visited = [start]
    queue = [start]
    while queue:
        room = queue.pop(0)
        if room == end:
            return True
        for r in school.get(room, []):
            if r not in visited:
                visited.append(r)
                queue.append(r)
    return False

root = None
for roll, name in [(5, "Aarav"), (2, "Mia"), (8, "Leo"), (1, "Zoe"), (4, "Sam")]:
    root = insert(root, roll, name)

while True:
    c = input("\n1.Add student 2.Search (BST) 3.Show all 4.Search (binary) 5.Check path between rooms 6.Exit\nchoice: ")
    if c == "1":
        root = insert(root, int(input("roll no: ")), input("name: "))
    elif c == "2":
        s = search(root, int(input("roll no: ")))
        print(s.name if s else "not found")
    elif c == "3":
        for s in inorder(root, []):
            print(s.roll, s.name)
    elif c == "4":
        s = binary_search(inorder(root, []), int(input("roll no: ")))
        print(s.name if s else "not found")
    elif c == "5":
        print(bfs(input("from room: "), input("to room: ")))
    elif c == "6":
        break