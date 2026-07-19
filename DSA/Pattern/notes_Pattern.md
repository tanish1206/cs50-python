1)Without Class and fxn the code will look like this 

N = 3

for i in range(N):

    for j in range(N):

        print("*", end=" ")

    print()

2) without class but with fxn the code will look like this 

def pattern1(N):

    for i in range(N):

        for j in range(N):

            print("*", end=" ")

        print()


pattern1(3)



3) what the end="" does ?

defualt print()
print("Apple")
print("Banana")
print("Cherry")

output
Apple
Banana
Cherry

with end=""
print("Apple", end=" ")
print("Banana", end=" ")
print("Cherry")

output 
Apple Banana Cherry

Explanation:

Print Apple
Instead of going to the next line, print a space
Print Banana
Again print a space
Print Cherry
Since the last print() uses the default end="\n", the cursor finally moves to the next line.

3) pattern 10 is an important one 

4) pattern 17 is imp one
