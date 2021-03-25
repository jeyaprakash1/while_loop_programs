# program for print a name if h is present in your name.

i=0
Name =input("Enter your Name")
length=len(Name)
while i<length:
    if Name[i]=='h':
        print(Name)
        break;
    i+=1
    
