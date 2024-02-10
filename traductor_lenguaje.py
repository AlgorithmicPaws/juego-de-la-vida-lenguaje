import os
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

def read_initial_states(directory, filenames, positions):
    initial_states = []
    for filename in filenames:
        filepath = os.path.join(directory, filename)
        print(filepath)
        with open(filepath, 'r') as file:
            lines = file.readlines()
            state = []
            for line in lines:
                state.append([int(x) for x in line.strip()])
            initial_states.append(np.array(state))
    concatenated_state = np.concatenate([initial_states[int(pos)] for pos in positions])
    return concatenated_state

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# List of filenames containing initial states
filenames = ['letra_pez.txt', 'letra_o.txt', 'letra_delta.txt', 'letra_d.txt', 'letra_b.txt']

# Get the positions from the user as a string
positions_str = input("Enter the positions of the arrays (0-5) to concatenate (e.g., '0123'): ")

# Convert the string to a list of positions
positions = [int(pos) for pos in positions_str]

# Read initial states from files and concatenate them
initial_state = read_initial_states(script_directory, filenames, positions)
print(initial_state)
# Run simulation
generations = 10
for generation in range(1, generations + 1):
    print("Generation", generation, ":")
    initial_state = next_state(initial_state)
    print_state(initial_state)
