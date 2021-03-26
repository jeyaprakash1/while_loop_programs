# print Numbers only from email id

Emailid=input("Enter your Email id")
length=len(Emailid)
i=0
while i<length:
    if Emailid[i]>='1' and Emailid[i]<='9':
        print(Emailid[i])
    i+=1
