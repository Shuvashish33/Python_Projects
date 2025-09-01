#using for loop
print('1+2+3+4+...+n')
n=int(input("Enter n="))
s=0
i=1
for i in range(s,n+1):
	s=s+i
	                #i=i+1 loop এ এটা use kora umnecessary
	print(s)
	
#এটার concise code
print(' concise code')

print('1+2+3+4+...+n')
n=int(input("Enter n="))
s=0 #s=1 hobe na
for i in range(1,n+1):
	s=s+i
	print(s)

print('\n1+3+5+7+...+n')
n=int(input("Enter n="))
s=0
for i in range(1,n+1,2):
	s=s+i
print(s)            
#এভাবে indentation করার কারনে অনলি final sum show করবে o/w প্রত্যেকটা value of sum show করবে

print('\n2+4+6+8+...+n')
n=int(input("Enter n="))
s=0
for i in range(2,n+1,2):
	s=s+i
print(s)
	
#Factorial! 
n=int(input("Factorial of N:"))
f=1
for i in range(1,n+1):
    f=f*i
print(f)