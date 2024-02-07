import numpy as np


def next_state(curr_state):
    height, width = curr_state.shape
    new_state = np.zeros((height, width), dtype=int)
    for y in range(height):
        for x in range(width):
            neighbors_sum = np.sum(curr_state[max(0, y-1):min(height, y+2), max(0, x-1):min(width, x+2)]) - curr_state[y, x]
            if curr_state[y, x] == 1 and not (2 <= neighbors_sum <= 3):
                new_state[y, x] = 0
            elif neighbors_sum == 3:
                new_state[y, x] = 1
            else:
                new_state[y, x] = curr_state[y, x]
    return new_state


def print_state(state):
    height, width = state.shape
    for y in range(height):
        for x in range(width):
            print(state[y, x], end=' ')
        print()
    print()

width, height = 5, 5
generations = 10

initial_state = np.array([[0, 0, 1, 0, 0],
                          [0, 1, 0, 1, 0],
                          [1, 0, 1, 0, 1],
                          [0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0]])


for generation in range(1, generations + 1):
    print("Generación", generation, ":")
    initial_state = next_state(initial_state)
    print_state(initial_state)
