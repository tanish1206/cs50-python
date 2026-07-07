class Solution:
    # Function to print the pattern
    def pattern4(self, N):
        # Outer loop for rows
        for i in range(1, N + 1):
            # Inner loop for columns
            # Print the row number 'i' in each column
            for j in range(1, i + 1):
                print(i, end=" ")
            # Move to the next row
            print()

if __name__ == "__main__":
    # Create object of Solution class
    sol = Solution()

    # Define size of pattern
    N = 5

    # Call pattern function
    sol.pattern4(N)
