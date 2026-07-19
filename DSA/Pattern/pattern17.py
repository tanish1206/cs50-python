class Solution:

    def pattern17(self,N):

        #for outer loops rows
        for i in range(N):

            #for printing spaces##for inner loops columns
            for j in range(N-1-i):
                print(" ", end="")
            #for printing stars
            for j in range(2*i+1):
                print(chr(65+j), end="")  
            #for printing spaces 
            for j in range(N-1-i):
                print(" ", end="")

            print()
sol=Solution()
N=5
sol.pattern17(N)



