class Solution:

    def pattern14(self,N):
    #outer rows
     for i in range(N):
      
      for j in range (i+1):
        print(chr(65+j), end=" ")
      print()  # Move to the next line after each row
     
    
sol = Solution()
N = 5# Set the size of the square (5x5)
sol.pattern14(N)  # Call the function to print the pattern




