#pass fail [if else]
m=int(input("Enter your marks:"))
if m>=33:
	print("pass")
else:
	print('fail')
print('Proggram terminated')


#odd even
n=int(input("Enter a number:"))
if(n%2==0):
	print(n,"is Even")
else:
	print(n,'is Odd')
print("Again terminated")


#GPA
m=60 #marks ইনপুট না নিয়ে default set korlam imput ও নেয়া যাবে। 
print("\n")
if m>=80:
	print("You have got an A+ and marks are",m)

elif m>=70:
	print("You have got an A and marks are",m)

elif m>=60:
	print("You have got an A- and the mark is",m)
	
elif m>=50:
	print("You have got an B",m)

elif m>=40:
	print("You have got an C",m)

else:
	print("You have failed ")