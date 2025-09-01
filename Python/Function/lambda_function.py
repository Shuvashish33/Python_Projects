#lambda function
a=lambda x,y : x+y
print(a(3,4))

#বা 
a=((lambda x,y: x+y)(4,3))
print(a)

#simplest
print((lambda x,y: x+y)(4,3))














'''
lambda x,y : x+y
print(lambda(3,4))
we can't call lambda function ny lambda()
cause lambda is not a function name but a function
'''