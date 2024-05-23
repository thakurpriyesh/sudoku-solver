import tkinter as tk
def is_valid(grid, row, col, num):
    # Check the row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check the column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check the box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if solve_sudoku(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

def print_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i!= 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j!= 0:
                print(" | ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

def solve_sudoku_gui():
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            entry = entries[i][j]
            value = entry.get()
            if value == "":
                row.append(0)
            else:
                row.append(int(value))
        grid.append(row)

    if solve_sudoku(grid):
        for i in range(9):
            for j in range(9):
                entry = entries[i][j]
                entry.delete(0, tk.END)
                entry.insert(0, grid[i][j])
    else:
        print("No solution exists")

root = tk.Tk()
root.title("Sudoku Solver")

entries = []
for i in range(9):
    row = []
    for j in range(9):
        entry = tk.Entry(root, width=3, font=("Arial", 16), justify="center")
        entry.grid(row=i, column=j)
        row.append(entry)
    entries.append(row)

solve_button = tk.Button(root, text="Solve", command=solve_sudoku_gui)
solve_button.grid(row=9, column=4, columnspan=5)

root.mainloop()