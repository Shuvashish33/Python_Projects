#Logical operator
'''
print("Enter three numbers:")
a =input() ইনপুট ফাংশন ডিফল্ট \n posses করে but এটা না চাইলে একসাথে ইনপুট নিতে হিবে
b =input()
c =input()
'''


  
  # Logical operator[and]
a, b, c = map(int, input("Enter three numbers with spaces: ").split())
if (a > b) and (a > c):
  print(a, "is the greatest number")
elif (b > a) and (b > c):
  print(b, "is the greatest number")
else:
  print(c, "is the greatest number")
print("Terminaed\n")  

#[ or ] vowel, consonant check

c=input("Enter a character (not capital):")

if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
	print("Vowel")
else:
    print("Consonant")
