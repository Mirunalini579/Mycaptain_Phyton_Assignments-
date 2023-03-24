n=int(input('Enter the total number of elements : '))
li=[]
for lp in range (1,n+1):
   x=int(input(f"Enter number {lp} :"))
   li.append(x)
print('The positive numbers are : ')
for lp in li:
    if lp>=0:
          print(lp,end=' ')
