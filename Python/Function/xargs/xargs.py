#xargs
def student(*details):
	print(details)
student(101, 'Anil')

#2
def student(*details):
	print(details[1])
student(101, 'Anil', 3.56)
student(103, 'APJ', 5.00)

#3
def add(*numbers):	                                  
	                                 #print(numbers)এটা                                       target না  এখানে
	    sum=0
	    for count in numbers:
	    	sum=sum+count
	    print(sum)
add(2,4)  
add(27,63,62)
add(17,27,27,73,24)
	              
	   