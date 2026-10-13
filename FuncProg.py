import numpy as np
from functools import reduce

def step(grid):
    new_grid = grid.copy()
    rows, cols = grid.shape
    for i in range(rows):
        for j in range(cols):
            neighbours = get_neighbours(grid, i, j)
            count = sum(neighbours)            
            # cells are unaffected unless they:
            # - die of under- or overpopulation, or
            # - become alive if they have exactly three neighbours
            if count < 2 or count > 3:
                new_grid[i, j] = 0
            elif count == 3:
                new_grid[i, j] = 1
    return new_grid
                 
def get_neighbours(grid, i, j):
    rows, cols = grid.shape
    indices = np.array([(i-1, j-1), (i-1, j), (i-1, j+1),
                        (i, j-1),             (i, j+1),
                        (i+1, j-1), (i+1, j), (i+1, j+1)])
    valid_indices = (indices[:, 0] >= 0) & (indices[:, 0] < rows) & \
                    (indices[:, 1] >= 0) & (indices[:, 1] < cols)
    return grid[indices[valid_indices][:, 0], indices[valid_indices][:, 1]]

# Test
grid = np.array([[0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 1, 1, 1, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0]], dtype=np.int8)
new_grid = step(grid)
print(new_grid)

# our grid should show a square pattern, but doesn't
expected_grid = np.array([[0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 0],
                          [0, 1, 0, 1, 0],
                          [0, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0]], dtype=np.int8)
assert np.array_equal(new_grid, expected_grid)


#Task 2
class Node(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.value = name
        self.children = children or []

    def __repr__(self):
        return f"Node({self.value}, {self.children})"

#    +
#   / \
#  1  *
#    / \
#   2   3
t = Node('+', [Node('1'),
               Node('*', [Node('2'),
                          Node('3')])])

def node_counter(tree):
    #start w 1
    node_number = 1
        #add 
    for child in tree.children:
        node_number += node_counter(child)
    return(node_number)

#a function that traverses the tree and returns the result of the expression
# so maybe it goes through and if
def evaluator(tree):
    if len(tree.children) == 0:
        return int(tree.value)
    else:
        child1 = evaluator(tree.children[0])
        child2 = evaluator(tree.children[1])
        if tree.value == '+':
            return child1 + child2
        elif tree.value == '-':
            return child1 - child2
        elif tree.value == '*':
            return child1 * child2
        elif tree.value == '/':
            return child1 / child2
        else:
            raise ValueError(f"Unknown operator: {tree.value}")

        
print(node_counter(t))
print(evaluator(t))

#TASK 3

def sum_of_squares(l):
    filtered = filter(lambda x: x[0]!='#', l)
    integers = map(int, filtered)
    squares = map(lambda x: x * x, integers)
    return reduce(lambda a, b: a + b, squares)

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))
print(sum_of_squares(['1', '2', '#100', '3']))

#Task 4
import time
from time import process_time_ns 
#Write a decorator which you can use to measure the 
#execution time of the decorated function using the 
# time.process_time_ns() function 

def decorator_time_measurer(func):

    def measure(*args, **kwargs):
        print('starting measuring time')
        result = time.process_time_ns()
        print('finished measuring time')
        return result
    return measure


@decorator_time_measurer
def measure_me(n):
    total = 0
    for i in range(n):
        total += i * i

    return total

print(measure_me(1000000))