class Solution:

    def pattern16(self,N):
    #outer rows
     for i in range(1,N+1):
      
      for j in range (1,i+1):
        print(chr(64+i), end=" ")
      print()  # Move to the next line after each row
     
    
sol = Solution()
N = 5# Set the size of the square (5x5)
sol.pattern16(N)  # Call the function to print the pattern