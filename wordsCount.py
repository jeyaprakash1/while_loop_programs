Sentence= "This is super very nice"
length=len(Sentence)
i=0
count=1
while i<length:
    if Sentence[i]==" ":
        count+=1
    i+=1
print("Total Number Of words are",count)
