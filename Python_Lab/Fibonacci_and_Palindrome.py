num = 121
rev = 0
n=num

while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed Number: " + str(rev))
if rev==n:
    print("Palindrome")
else:
    print("not a palindrome")

#Fibonacci
a=0
b=1
c=1
while a<10:
    a=b
    b=c
    c=a
    print(c)
    c=a+b
    a+=1
