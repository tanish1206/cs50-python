class Solution:

    def pattern5(self,N):
    #outer rows
     for i in range(N):
      
      for j in range (N-i):
        print("*", end=" ")
      print()  # Move to the next line after each row
     
    
sol = Solution()
N = 5# Set the size of the square (5x5)
sol.pattern5(N)  # Call the function to print the pattern


