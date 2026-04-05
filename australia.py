# Map Coloring - Australia
all_states = ["WA", "NT", "Queensland", "SA", "NSW", "V", "T"]
available_colors = ["Red", "Green", "Blue"]

adjacencies = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Queensland"],
    "SA": ["WA", "NT", "Queensland", "NSW", "V"],
    "Queensland": ["NT", "SA", "NSW"],
    "NSW": ["Queensland", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}
def is_valid(state, color, assignments, neighbors):
    for neighbor in neighbors[state]:
        if neighbor in assignments and assignments[neighbor] == color:
            return False
    return True

def solve_map_coloring(assignments, states, colors, neighbors):
    if len(assignments) == len(states):
        return assignments

    current_state = states[len(assignments)]

    for color in colors:
        if is_valid(current_state, color, assignments, neighbors):
            assignments[current_state] = color
            
            result = solve_map_coloring(assignments, states, colors, neighbors)
            if result:
                return result
            
            assignments.pop(current_state)
            
    return None

solution = solve_map_coloring({}, all_states, available_colors, adjacencies)

if solution:
    for state in solution:
        print(state + ": " + solution[state])
else:
    print("No solution could be found.")
