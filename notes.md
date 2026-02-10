here the notes that i learned from the week 1 


hello world :
print("hello world")

*comment = ## this for a single sentence or """ """and this can be used if there are multiple lines of comment

to take a input from the user !
name = input("whats your name?")
print("hello," +name )


*remove white space from the user name 
name = name.strip()
  ##with this u can remove the blank spaces that are present or is mistaken by the user 

#Capitalize user name 
name = name.capitalize()
         ## this will only capitalise the 1st letter of the word the drawback is that it will print "Tanish soni " not "Tanish Soni"

name = name.title()
     ## this will print "Tanish Soni"

*special way to represent string

print(f"hello,{name}")
  this will output  hello name(function ka input )
  here f is used to give a hint to the ide or computer that we have treat the {} as a special function
  