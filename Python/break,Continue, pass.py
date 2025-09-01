#break, contininue, pass
av=5
x=int(input("How many candies you want?:"))
i=1
while i<=x:
	if i>av:
		print("No more stock, try again later")
		break
	print('Here you go!')
	i+=1
#if x>av:
av=5
x=int(input("How many candies you want?:"))
i=1
while i<=x:
	if x>av:
		print("Insufficient Gold💰 ")
		break
	print('Purchased Succesful!💸')
	i+=1

#continue
for i in range(1,101):
	if i%3==0  or i%5==0:
		continue
	print(i)

#pass
for i in range(1,101):
	if i%3==0 or i%5==0:
		pass
	else:
		print('\n\n',i)