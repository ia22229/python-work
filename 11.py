def f(i=0,j=1,k=):
    if j>n:
        return
    print(i,end=" ")
    f(k,j+1,i+k) 
n= int(input("enter how many numbers to print : "))
f(0,1,1)
