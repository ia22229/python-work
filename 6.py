num = int(input("Enter a number : "))
factorial = 1
for i in range(num,0,-1) :
    factorial *= i
print("The factorial of ", num, " is : ", factorial)


str1 = input("Enter a string : ")
str2 = ""
l1 = len(str1)
for i in range(l1-1,-1,-1) :
    str2 += str1[i]
print("The reverse of the string is : ", str2)
   
   
num1 = int(input("Enter the number : "))
j = str(num1)
sum = 0
for i in j :
    i = int(i)
    sum += i
print("The sum  is : ", sum)
