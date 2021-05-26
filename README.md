# Logic of the program

The program uses simple OOP concepts to create a tictactoe game    

*All design decisions are explained in quotes following the explanation of each module 
***

## main.py

1. The main file uses a 2-d array `arr` to store the current values of each element in the grid. Values are stored as 0 for an unmarked square, 1 for player one's input and 2 for player two's input

2. The program then takes the input from the user, updates the array `arr` with the input and uses the `print_grid` method of the `grid` class to print the grid ( _refer to **grid_mod.py**_ )

3. The program then uses the `grid_checker` function to check if the game has ended and to evaluate the result

>I used these separate functions to make debugging easier and to make the whole program modular. If the user input is not a valid square, the loop is repeated without incrementing the value of i in order to take the input of the same user again after displaying the appropriate error message

***
## grid_mod.py

A class `grid` is defined here which has attributes as follows:   
1. `self.x`, `self.o`, `self.none` store each line of the grid input in a string array  
> I used a string array to make it easy to print the grid elements according to the given format. This way, using a simple while loop,I can break down the elements into lines of 5 and print it along with the borders according to my convenience

2. `self.dict` is a dictionary that is used by `print_grid` to convert the user input (0,1,2) to the appropriate array elements from `self.x`, `self.o`, and `self.none`
>I used a dictionary here as it makes it easier to choose which array to pass to `print_grid`'s loops according to the user input from **main.py**. 

3. `print_grid` is a class method which uses `self.dict` and `self.arr` to print the grid
>Here I used the character array above to print every line of the grid, having broken each grid element into 5 lines. Horizontal and vertical borders are also easy to print this way according to the given format.

4. `grid_checker` evaluates the grid after each player input to check if the game has ended and returns the result.
>Defining this function here as an attribute to the `grid` object makes it easier to call it in **main.py** and makes the code compact and more efficient.

***

