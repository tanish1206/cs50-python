class Solution:

    def pattern15(self,N):
    #outer rows
     for i in range(N,-1,-1):
      
      for j in range (i+1):
        print(chr(65+j), end=" ")
      print()  # Move to the next line after each row
     
    
sol = Solution()
N = 5# Set the size of the square (5x5)
sol.pattern15(N)  # Call the function to print the pattern


