import os
x=int(input("Enter the number"))
match x:
    case 0:
        print("its 0")
    case 2:
        print("its 2")
    case _:
        print("its default")