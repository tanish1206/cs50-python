class Solution:
    # Function to print the pattern of alphabets
    def pattern14(self, N):
        # Outer loop for the number of rows
        for i in range(N):
            
            # Inner loop to print alphabets from A to A + i
            for j in range(i + 1):
                print(chr(65 + j), end=" ")  # Print the alphabet character followed by a space

            # Move to the next line after printing the current row
            print()

# Driver code
sol = Solution()
N = 5  # Set the size of the pattern (5 rows)
sol.pattern14(N)  # Call the function to print the pattern
