class Solution:
    # Function to print Pattern 11
    
    def pattern11(self, n):
        for i in range(n):
         #for outer column
            for j in range(i+1):
            #for inner column
                if i % 2 == 0:
                    i=1
                #even place of outer column  when even 
                #place 1
                else:
                    i=0
                #odd place of outer column when odd place 0
                print(i, end=' ')
            print()
#and further more when in column n=1 j =2 therefore even 
#thus 1 is printed = 0 1 
sol = Solution()
    # Define N
N = 5
    # Call pattern function
sol.pattern11(N)
