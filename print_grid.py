class grid:
   def __init__(self,arr):
      self.arr = arr
      self.x = [" xx      xx ","   xx  xx   ","     xx     ","   xx  xx   "," xx      xx "]
      self.o = ["    oooo    ","  oo    oo  "," oo      oo ","  oo    oo  ","    oooo    "]
      self.none = ["            ","            ","            ","            ","            "]
      self.dict = {0:self.none,1:self.x,2:self.o}
      self.vline = ["|","|","|","|","|"]                                                               #REMOVE?
      self.hline = "---------------|--------------|---------------"

   def print_grid(self):
      for i in range(3):
         for j in range(5):
            print('|',self.dict[self.arr[i][0]][j],'|',self.dict[self.arr[i][1]][j],'|',self.dict[self.arr[i][2]][j],'|')  #Prints each line in the output 
         if i < 2:
            print(self.hline)

   def grid_checker(self):
      for i in range(3):
         if (self.arr[i][0] == self.arr[i][1] and self.arr[i][1] == self.arr[i][2]):           
            return self.arr[i][0]
         elif (self.arr[0][i] == self.arr[1][i] and self.arr[1][i] == self.arr[2][i]):         
            return self.arr[0][i]
      if (self.arr[0][0] == self.arr[1][1] and self.arr[1][1] == self.arr[2][2]):
         return self.arr[1][1]
      elif (self.arr[0][0] == self.arr[1][1] and self.arr[1][1] == self.arr[2][2]):           
         return self.arr[1][1]
      else:
         return 4
            