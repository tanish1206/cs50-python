name = input("What is your name? ")

match name:
    case "Harry" | "hermione" | "ron":
        print("gryffindor  ")
    
 
    case "draco":
        print("slytherin  ")
    case _:
        print("who")
