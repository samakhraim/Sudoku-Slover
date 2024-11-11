
# Sudoku Solver

This is a Sudoku solver built using Python and Pygame. The application uses a backtracking algorithm to solve the given Sudoku puzzle and displays the solution in a graphical interface.

## Features

- **Sudoku Solver**: Automatically solves any valid Sudoku puzzle using a backtracking algorithm.
- **Pygame Display**: Shows the Sudoku puzzle and its solution in a Pygame window with a clean visual layout.
- **Interactive Grid**: Sudoku numbers are displayed on a 9x9 grid with thicker lines marking the 3x3 boxes.

## Requirements

- **Python 3.x**
- **Pygame**: For graphical display of the board.

## Installation

1. **Clone or Download** this repository.
2. Install the required libraries using pip:

    ```bash
    pip install pygame
    ```

## Usage

1. **Edit the Puzzle**: Open the code and set your Sudoku puzzle in the `board` variable. The default puzzle provided in the code is:

    ```python
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    ```
   Replace the zeros (`0`) with the numbers in your puzzle, leaving the zeros for cells to be solved.

2. Run the program:

    ```bash
    python sudoku_solver.py
    ```

3. The program will open a Pygame window displaying the Sudoku puzzle and then attempt to solve it. If a solution is found, it will display the completed board in the window.

4. To exit, close the Pygame window.

## Code Overview

- **`solve_sudoku(board)`**: A backtracking function that fills in empty cells with numbers from 1 to 9, ensuring each cell placement follows Sudoku rules.
- **`draw_grid()`**: Draws the 9x9 Sudoku grid, with thicker lines dividing each 3x3 sub-grid.
- **`draw_numbers(board)`**: Displays numbers on the board in the Pygame window.
- **`is_valid(board, num, pos)`**: Validates if a number can be placed in a specific cell without conflicting with other numbers in the same row, column, or 3x3 sub-grid.

## Example Board

The default board used in the code is:

```python
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
```

## How It Works

The code solves the Sudoku puzzle using a backtracking algorithm, which involves:

1. **Finding an Empty Cell**: It searches for an empty cell (marked as `0`).
2. **Trying Numbers**: For each empty cell, it tries numbers from 1 to 9, checking if each number is valid.
3. **Recursion and Backtracking**: If placing a number leads to a dead end (i.e., no valid numbers left for a cell), the function backtracks, removing the number and trying the next one.
4. **Completing the Board**: If all cells are filled, the puzzle is solved.

## How It Look Like
![image](https://github.com/user-attachments/assets/433d22d0-1fd4-461b-885b-565f2da53e0b)



## Acknowledgments

- Inspired by Sudoku-solving algorithms and Pygame tutorials.
- [Pygame Community](https://www.pygame.org/contribute.html) for graphics support in Python projects.
