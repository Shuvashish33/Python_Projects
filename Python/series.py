print('1+2+3+4+...+n')
n=int(input("Enter n="))
s=0
i=1
while i<=n:
	s=s+i
	i=i+1
	print(s)

print('\n1+3+5+7+...+n')
n=int(input("Enter n="))
s=0
i=1
while i<=n:
	s=s+i
	i=i+2
print(s)  #এভাবে indentation করার কারনে অনলি final sum show করবে o/w প্রত্যেকটা value of sum show করবে

print('\n2+4+6+8+...+n')
n=int(input("Enter n="))
s=0
i=2
while i<=n:
	s=s+i
	i=i+2
	print(s)
	
#Factorial! 
n=int(input("Factorial of N:"))
f=1
i=1
while i<=n:
    f=f*i
    i+=1
print(f)