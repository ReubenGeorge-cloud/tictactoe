from grid_mod import grid

# store the values of each grid element as 0,1,2
arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
grid = grid(arr)
grid.print_grid()  # prints the grid with current values from arr
i = 0

while(i < 9):
    try:
        row = int(input("Enter the row name: "))  # taking input
        col = int(input("Enter the column name: "))
        if(arr[row][col] == 0):  # checking if square is unmarked before marking
            if(i % 2):
                arr[row][col] = 2  # marks square with player 1's symbol (x)
            else:
                arr[row][col] = 1  # marks square with player 2's symbol (o)
            i += 1  # i increments only if the square was unmarked
        else:
            print("\nThat square has already been marked! Please select another square")
            continue
    except IndexError:
        print("\nThat square is not available. Please select a valid square")
    grid.print_grid()
    res = grid.grid_checker()  # grid_checker func to check if a player has won
    if (res == 1):
        print("\nPlayer 1 wins the game!")
        break
    elif(res == 2):
        print("\nPlayer 2 wins the game!")
        break
    elif(i == 9):  # draws and ends the game when all squares have been marked
        print("\nThe game has ended in a draw!")
