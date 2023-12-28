def matrix(N):
    matrix = [[0] * N for _ in range(N)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    direction = 0  # Start with moving right
    row, col = 0, 0

    for num in range(1, N * N + 1):
        matrix[row][col] = num

        # Calculate the next position
        next_row, next_col = row + directions[direction][0], col + directions[direction][1]

        # Change direction if next position is out of bounds or already visited
        if (
                next_row < 0 or next_row >= N or
                next_col < 0 or next_col >= N or
                matrix[next_row][next_col] != 0
        ):
            direction = (direction + 1) % 4  # Change direction clockwise
            next_row, next_col = row + directions[direction][0], col + directions[direction][1]

        row, col = next_row, next_col

    return matrix

if __name__ == '__main__':
    print(matrix(3))
