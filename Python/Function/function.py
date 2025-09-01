#function
#1
def greet():
	print("Hello")
	print("Good Morning")
greet()

#2
def add(x,y):
	print(x+y) 
add(5,7)

#3
def add_sub(a,b):
    c=a+b
    d=a-b
    return c,d
#calling the function
r1,r2=add_sub(7,6)
print(r1,r2)