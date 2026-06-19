# balance=10000
# while True:
#     n=int(input("1 for Withdraw\n2 for Balance\n3 for Deposit\n4 for exit \nChoose above options : "))
#     def withdraw(cash,balance):
#         if cash<=0:
#             print("\nInvalid Withdrawal Amount")
#         elif cash <= balance:
#             balance-=cash
#             print("\nWithdrawl Successful")
#         else :
#             print("\n Withdrawal Failed Due to 4Insufficient balance")
#         return balance
        
#     def balance1():
#         print(f"\nYour Bank balance is {balance}\n")
        
#     def deposit(cash,balance):
#         if cash>0:
#             balance+=cash
#             print("\nDeposit successful")
#         else:
#             print("\nInvalid Deposit")
#         return balance

#     if n==1:
#         cash=int(input("\nEnter the amount to  withdraw : "))
#         balance=withdraw(cash,balance)
#         balance1()
#     elif n==2:
#         balance1()
#     elif n==3:
#         cash=int(input("\nEnter the amount to  deposit : "))
#         balance=deposit(cash,balance)
#         balance1()
#     elif n==4:
#         break
#     else :
#         print("\nInvalid Request\n")


# matrix = {
#     (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(1,1),(2,1),(3,1),(4,1),(5,1),(2,2),(3,2),(4,2),(3,3)
# }
# print()
# for i in range (7):
#     for j in range(4):
#         if (i,j) in matrix:
#             print("*",end="  ")
#         else :
#             print(end="  ")
#     print()
# print()

# matrix = {
#     (0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(1,2),(2,2),(3,2),(4,2),(5,2),(2,1),(3,1),(4,1),(3,0)
# }
# print()
# for i in range (7):
#     for j in range(4):
#         if (i,j) in matrix:
#             print(" ",end="*")
#         else :
#             print(end="  ")
#     print()
# print()



# row = int(input("Enter the number of rows : "))
# if row %2==0:
#     row+=1
# for i in range ((row//2)+1):
#     for j in range((row//2)+1):
#         if i>=j :
#             print("*",end="  ")
#     print()
# for i in range ((row//2),0,-1):
#     for j in range((row//2),0,-1):
#         if i>=j:
#             print("*",end="  ")
#     print()

# row = int(input("Enter the number of rows : "))
# j=0
# if row%2==0:
#     row+=1
# for i in range (row):
#     if i<=(row/2):
#         print("  "*(((row//2)+1)-i)," *"*(i+1))
#         j+=1
#     else :
#          print("  "*(((row//2)+3)-j)," *"*(j-1))
#          j-=1

matrix = {
    (0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(1,2),(2,2),(3,2),(4,2),(5,2),(2,1),(3,1),(4,1),(3,0)
}
print()
for i in range (7):
    for j in range(4):
        if (i,j) in matrix:
            print("*",end="  ")
        else :
            print(end="   ")
    print()
print()
