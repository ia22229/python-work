row = int(input("Enter the number of rows : "))
for i in range(1,row+1):
    print(" "*(row-i),"* "*(i))
    
# j=0
# for i in range(1,row+1):
#     print(" "*(row-i),"*"*(i+j))
#     j+=1

# for i in range(1,row+1):
#     for j in range(row-i):
#         print(" ",end='')
#     print("* "*i)
    
# for i in range(1,row+1):
#     for j in range(row-i):
#         print(" ",end='')
#     for i in range(i):
#         print("* ",end='')
#     print()