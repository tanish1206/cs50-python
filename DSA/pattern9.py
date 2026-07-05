class Solution:
    # Function to print a square pattern of stars
    def pattern9(self, N):
    
        # Outer loop for rows
        for i in range(N):

            # Print leading spaces
            for j in range(N - i - 1):
                print(" ", end="")

            # Print stars
            for j in range(2 * i + 1):
                print("*", end="")

            # Print trailing spaces
            for j in range(N - i - 1):
                print(" ", end="")
           

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
    sol.pattern9(N)

