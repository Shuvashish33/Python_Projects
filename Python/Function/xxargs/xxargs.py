#xxargs
def student(**details):
	print(details)
student(id=101, name='Anil')

#2
def student(**details):
	print(details['id'])
student(id=101,name= 'Anil',gpa= 3.56)


#xargs not xxargs
def add(*numbers):	                                  
	                                 #print(numbers)এটা                                       target না  এখানে
	    sum=0
	    for count in numbers:
	    	sum=sum+count
	    print("\n\t",sum)
add(2,4)  
add(27,63,62)
add(17,27,27,73,24)
	              
	   