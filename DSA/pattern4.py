class Solution:

    def pattern4(self,N):
    #outer rows
     for i in range(1,N+1):
     #inner columns 
      for j in range (1,i+1):
        print(j, end=" ")

      print()  # Move to the next line after each row
    
sol = Solution()
N = 5# Set the size of the square (5x5)
sol.pattern4(N)  # Call the function to print the pattern


