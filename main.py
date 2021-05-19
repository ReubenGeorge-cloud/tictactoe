from print_grid import grid

arr = [[0,0,0],[0,0,0],[0,0,0]]
grid = grid(arr)
grid.print_grid()

for i in range(9):
    row = int(input("Enter the row name: "))
    col = int(input("Enter the column name: "))
    if(i%2):
        arr[row][col] = 1
    else:
        arr[row][col] = 2
    grid.print_grid()