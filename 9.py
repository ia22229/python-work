# num = int(input("Enter  a number :"))
# str = str(num)
# length = len(str)
# str1=''
# for i in range(length-1,-1,-1):
#     str1+=str[i]
# num1=int(str1)
# if num1 == num :
#     print("palidrome")
# else :
#     print("Not Palidrome")
    
    
# password ={
#     ("user1","123"),("user2","456"),("user3","789")
# }
# j=0
# for i in range(3):
#     user = input("Enter the username :")
#     pass1 = input("Enter the password :")
#     if (user,pass1) in password :
#         print("successful")
#         break
#     else :
#         j+=1
#         print("Username or password is incorrect")
# if j==3 :
#     print("Your 3 attempt is over")


# for i in range(1,101):
#     if i%3==0 and i%5==0 :
#         print("Both")
#     elif i%3==0 :
#         print("Three")
#     elif i%5==0 :
#         print("Five")
#     else :
#         print(i)


# sub=[]
# mark=0
# for i in range(5):
#     num = int(input("enter the mark for subject " + str(i+1) + " in 100 marks : "))
#     sub.append(num)
#     mark+=num
# marks=mark/5
# if marks>=90:
#     print("A")
# elif marks>=75:
#     print("B")
# elif marks>=50:
#     print("C")
# else :
#     print("Fail")


num = int(input("Enter a number :"))
j=0
for i in range(1,num):
    if num%i==0 :
        j+=i
if j==num :
    print("it is a perfect number")
else :
    print("it is not perfect number")