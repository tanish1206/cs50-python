class Solution:

    def pattern18(self,N):

        #for outer loops rows
     for i in range(N):
      
      for j in range(i+1):
        print(chr(65+N-i-1+j), end=" ")  
        # Print letters in reverse order

         #for inner loops columns
        

          

      print()
sol=Solution()
N=5
sol.pattern18(N)



