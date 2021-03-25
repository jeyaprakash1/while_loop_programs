#program for print consonants in given name and its count

i=0
count=0
Name=input("enter your name")
length=len(Name)
while i<length:
    if Name[i] not in ['a','e','i','o','u']:
        print(Name[i])
        count+=1
    i+=1
print("Total count of consonants is",count)
