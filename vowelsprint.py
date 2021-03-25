# program for vowels count in given name, and print those vowels

i=0
count=0
Name=input("Enter your name")
length=len(Name)
while i<length:
    if Name[i] in ['a','e','i','o','u']:
        print(Name[i])
        count+=1
    i+=1
print("Total count is",count)
