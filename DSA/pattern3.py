class solution:

    def pattern3(self,N):
        for i in range(1,N+1):

            for j in range(i,i+1):
                print("* " * j)