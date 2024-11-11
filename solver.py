import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Fonts
FONT = pygame.font.SysFont("arial", 40)

# Initial board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Draw grid lines
def draw_grid():
    for i in range(10):
        line_width = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * 66), (WIDTH, i * 66), line_width)
        pygame.draw.line(screen, BLACK, (i * 66, 0), (i * 66, HEIGHT), line_width)

# Draw numbers on the board
def draw_numbers(board):
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                text = FONT.render(str(num), True, BLUE)
                screen.blit(text, (col * 66 + 20, row * 66 + 10))

# Find an empty cell in the board
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

# Check if placing a number is valid
def is_valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

# Solve the board using backtracking
def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

# Main function to run the game
def main():
    # Solve the Sudoku puzzle
    if solve_sudoku(board):
        print("Sudoku solved successfully.")
    else:
        print("No solution exists.")

    # Game loop
    running = True
    while running:
        screen.fill(WHITE)
        draw_grid()
        draw_numbers(board)  # Draw the solved board

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()  # Update the display

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
