class Solution:
    # Function to print a square pattern of stars
    def pattern8(self, N):
    
        # Outer loop for rows
        for i in range(N):

         #for lending space 
         for j in range(i):
            print(" ", end="")
         for j in range(N+4-2*i):
            print("*", end="")
         for j in range(i):
             print(" ", end="")
         print()  # Move to the next line after each row

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern8(N)

