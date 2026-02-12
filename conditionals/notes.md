1) if = it will go through all the conditions even if the 1st condtional is satisfied
elif = if the condition is satisfied all good , but if not it will check other condition
else = if the above condtion is not satisfied it doesnt care and will print the condition present in it

x = int(input("value of x is ?:"))
y = int(input("value of y is ?:"))

if x>y:
    print("x is greater than y")

elif x<y :
    print("x is less than y")
else:
    print("x is equal to y")
    
2) or operator
same starting 2 lines  as 1)
if x>y or x<y:
    print("x is not equal to y")
else:
    print("x is equal to y")

3) types of conditionals 
and = act as a conjunction 
!= = not equal to 
<= = less than equal to and vise versa

4) score = int(input("whats your score?"))

if score >=90 and score <= 100:
    print ("you got a A")

elif score >=80 and score < 90:
    print ("you got a B") 

elif score >=70 and score < 80:
    print ("you got a C")
elif score >=60 and score < 70:
    print ("you got a D") 
else :
    print ("you got a F")
    
