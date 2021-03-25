# program for print a name without 'H' if 'H' is present.


i=0
Name=input("Enter your name")
length=len(Name)
while i<length:
    if Name[i]=='h':
        i+=1
        continue
    print(Name[i])
    i+=1    
     
