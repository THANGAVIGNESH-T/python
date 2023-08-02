a=[22,45,66,56,43,33,33]
print("values divisible by 3:")
for num in a:
    if num%3==0:
        print(num)
for num in a:
    if num%2==0:
        print(num**2)       
sum=0
for x in a:
   if x%2==0:
        sum=sum+x
print("sum of digits of all even numbers",sum)  

noduplicate=[]
for num in a:
    if num not in noduplicate:
        noduplicate.append(num)
print(noduplicate)