#python program to print the count of numbers entered by the user

n=int(input("entre number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("the number of digits entered by the user:",count)