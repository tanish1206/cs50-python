here the notes that i learned from the week 1 


1) hello world :
print("hello world")

2) *comment = ## this for a single sentence or """ """and this can be used if there are multiple lines of comment

3) to take a input from the user !
name = input("whats your name?")
print("hello," +name )


4) *remove white space from the user name 
name = name.strip()
  ##with this u can remove the blank spaces that are present or is mistaken by the user 

5) #Capitalize user name 
name = name.capitalize()
         ## this will only capitalise the 1st letter of the word the drawback is that it will print "Tanish soni " not "Tanish Soni"

6) name = name.title()
     ## this will print "Tanish Soni"

*special way to represent string

print(f"hello,{name}")
  this will output  hello name(function ka input )
  here f is used to give a hint to the ide or computer that we have treat the {} as a special function

  run the code with this prompt on the terminal :"python .\basics.py"


7) float functions 
round(x+y)
              will help to round the float value up to 2 digits 
  round (x+y,2)
             will give 2 decimal points as the answer
            
8) fuctions
  syntax =  def():
example:
  def hello(to):
    print("Hello, " + to)   

name = input("whats your name")
hello(name)
out put = hello, tanish

 def hello(to="world")
     print ("hello,"+to)
  
hello()        // here we have set a fix parameter just in case if the user (coder) doesnt give a parameter
output = hello,world


9) 1st solution 
def main():
    x = int(input("whats value of x? "))
    print("x squared is " + str(square(x)))
    
def square(x):
    return x*x 

main()

2nd solution 
def main():
    x = int(input("whats value of x? "))
    print("x squared is " + str(square(x)))
    
def square(x):
    return x*x 

main()

10) there were some basic error like i cant write print("x squared is " + int(square(x)))
       why ? = because u cant have string  ="x squared is " with int inegration in a same print command 