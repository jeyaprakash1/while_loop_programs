# program for finding greatest common divisor in given two numbers

no1=int(input("Enter Number"))
no2=int(input("Enter Number"))
i=1
if no1>no2:
   small=no2
elif no2>no1:
   small=no1
while small>i:
    if no1%small==0 and no2%small==0:
        print("greatest is",small)
        break;
    small-=1

