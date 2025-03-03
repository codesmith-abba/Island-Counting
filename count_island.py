from util import Node, QueueFrontier

# 1 ---> Land
# 0 ---> Water

def count_island(gridList):
    """
    Counts the number of islands in the grid using BFS.
    """
    if not gridList:
        return 0

    rows, cols = len(gridList), len(gridList[0])
    island_count = 0

    # Helper to mark the entire island as visited using BFS
    def explore_island(start):
        frontier = QueueFrontier()
        frontier.add(Node(state=start, parent=None, action=None))
        while not frontier.empty():
            node = frontier.remove()
            row, col = node.state
            for action, (new_row, new_col) in get_neighbors((row, col), rows, cols):
                if gridList[new_row][new_col] == 1:  # Land
                    gridList[new_row][new_col] = 0  # Mark as visited
                    frontier.add(Node(state=(new_row, new_col), parent=None, action=action))

    # Traverse the grid
    for row in range(rows):
        for col in range(cols):
            if gridList[row][col] == 1:  # Found unvisited land
                explore_island((row, col))  # Explore the island
                island_count += 1  # Increment island count

    return island_count


def get_neighbors(state, rows, cols):
    """
    Finds valid neighbors (up, down, left, right) for the given cell.
    """
    row, col = state
    neighbors = [
        ('Up', (row - 1, col)),
        ('Down', (row + 1, col)),
        ('Left', (row, col - 1)),
        ('Right', (row, col + 1))
    ]
    valid_bounds = []
    for action, (r, c) in neighbors:
        if 0 <= r < rows and 0 <= c < cols:  # Check bounds
            valid_bounds.append((action, (r, c)))
    return valid_bounds


# Example Usage
gridList = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]

print("Number of islands:", count_island(gridList))
