# Creating a function
def sum(a, b):
    add= a+b
    print(add)
    
    
def isGreater(a, b):
    if(a>b):
        print("A is greater than B")
    else: 
        print("B is greater than A")
# jb hume function toh bna diya h pr uski body bd m likhna h tb hum "pass" keyword ka use krte hai..   
def isLess(a, b):
    pass


def average(*numbers):
    sum =0 
    for i in numbers:
        sum += i
    print("Average is: ", sum/len(numbers))
# a=19
# b=1
# sum(a,b)
# isGreater(a,b)
# c=10
# d=18
# sum(c,d)
# isGreater(c,d)

# average(10,20, 30)

def average1(*numbers):
    sum =0 
    for i in numbers:
        sum += i
    return sum/len(numbers)
    
printingTheValues= average1(10,20,30)
print(printingTheValues)

