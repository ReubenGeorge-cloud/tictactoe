class grid:
    def __init__(self,arr):
        self.arr = arr        # 2-D array containing the values of grid elements
    
    def print_grid(self):       #printing the grid with dictionary keys
        print("\n ",self.dict[1]," | ",self.dict[2]," | ",self.dict[3]," \n_____ _____ _____\n\n ",self.dict[4]," | ",self.dict[5]," | ",self.dict[6],"\n_____ _____ _____\n\n ",self.dict[7]," | ",self.dict[8]," | ",self.dict[9], "\n")

    def grid_checker(self):     #function for checking if a player has won. Returns boolean value
        for i in range(7):      #checking the rows
            if(self.dict[i] == self.dict[i+1] and self.dict[i+1] == self.dict[i+2]):
                return True
            else:
                for i in range(3):      #checking the columns
                    if(self.dict[i] == self.dict[i+3] and self.dict[i+3] == self.dict[i+6]):
                        return True
                    else:               #checking the diagonals
                        if(self.dict[1] == self.dict[5] and self.dict[5] == self.dict[9]):
                            return True
                        elif(self.dict[3] == self.dict[5] and self.dict[5] == self.dict[7]):
                            return True
                        else:
                            return False
