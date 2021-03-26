# get number of subjects and it's total and it's average

subjects = int(input("Enter number of subjects"))
total=0
sub2=subjects
while subjects>0:
    Mark=int(input("Enter your mark"))
    total=total+Mark
    subjects-=1
print("Your total is",total)
print("Your average is",total//sub2)
    

