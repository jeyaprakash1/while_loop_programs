# program for common divisors of two number like 100 and 75

no1=int(input("Enter Number"))
no2=int(input("Enter Number"))
i=1
if no1>no2:
   small=no2
elif no2>no1:
   small=no1
while i<small:
    if no1%i==0 and no2%i==0:
        print(i)
    i+=1

