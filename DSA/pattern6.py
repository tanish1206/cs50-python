class Solution:
    # Function to print a square pattern of stars
    def pattern6(self, N):
    
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

            # Move to next row
            print()

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern6(N)

