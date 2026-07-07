class Solution:

    def pattern12(self, N):

        for i in range(N):

            # Left numbers
            for j in range(i + 1):
                print(j + 1, end="")

            # Middle spaces
            for j in range(2 * (N - i - 1)):
                print(" ", end="")

            # Right numbers
            for j in range(i, -1, -1):
                print(j + 1, end="")

            print()


sol = Solution()
sol.pattern12(4)