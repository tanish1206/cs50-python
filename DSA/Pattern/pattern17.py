class Solution:

    def pattern17(self,N):

        #for outer loops rows
        for i in range(N):

            #for printing spaces##for inner loops columns
            for j in range(N-1-i):
                print(" ", end="")

            #for increasing letters
            for j in range(i+1):
                print(chr(65+j), end="")  

            #for decreasing letters
            for j in range(i-1,-1,-1):
                print(chr(65+j), end="")

            #for printing spaces 
            for j in range(N-1-i):
                print(" ", end="")

            print()
sol=Solution()
N=4
sol.pattern17(N)



