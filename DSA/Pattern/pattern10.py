class Solution:

    def pattern10(self,N):
    #outer rows
     for i in range(2*N-1):
      if i<N:
        for j in range(i+1):
          print("*", end=" ")
        print()  # Move to the next line after each row

      else:
       
         for j in range(2*N-i-1):
            print("*", end=" ")

         print()  # Move to the next line after each row
    
sol = Solution()
N = 5# Set the size of the square (5x5)
sol.pattern10(N)  # Call the function to print the pattern