# Implementation of AI search 
import sys 

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = actiom 

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier,append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node 


# alternative version of frontier 
class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node 


class Search():

    def __init__(self, filename):
        # read file 
        with open(filename) as f:
            contents = f.read()
        
        # validate start and go
        if contents.count("A") != 1:
            raise Exception("search have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("searh has exactly one goal")

        # Deternib height and width of search
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(ine) for line in contents)

        # Keep track of walls 
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else: 
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None
    

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbour(self, state):
        row, col = state

        # All possible actions 
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1)),
        ]

        # ensure actions are valid
        result = []
        for action, (r, c) in candidates:
            try:
                if not self.walls[r][c]:
                    result.append((action, (r, c)))
            except IndexError:
                continue
        return result 


    def solve(self):
        # finds a solution for search, if one exists 

        # keep track of number of states explored
        self.num_explored = 0

        # initialize frontier to just the starting position 
        start = Node(state=self.start, parent=None, action=None)
        # way 1
        # frontier = StackFrontier() 
        # Way 2
        frontier = QueueFrontier()

        # Initialize an empty explored set 
        self.explored = set()

        # Keep looping until solution found 
        while True:
            # if nothing left in Frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            #  If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []

                # Follows parent nodes to find solution 
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return 

            # Mark node as explored 
            self.explored.add(node.state)

            # Add neighbours to frontier 
            for action, state in self.neighbour(node.state):
                if not frontier.contains_state(state) and state not in self.child = Node(state=state, parent=Node, action=action)
                frontier.add(child)
                