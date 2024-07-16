num1=input("Enter the number:")
num2=input("Enter the number:")
num3=input("Enter the number:")
if num1==num2==num3:
    print("Equilateral triangle")
elif num1==num2 or num1==num3 or num3==num3:
    print("Isoceleus triangle")
else:
    print("Scalene triangle")

user1=input("Enter the name:")
user2=input("Enter the name:")
if user1==user2:
    print("Draw")
elif user1=="Rock" and user2=="Paper":
    print("Paper won")
elif user1=="Paper" and user2=="Scissor":
    print("Scissor won")
elif user1=="Scissor" and user2=="Rock":
    print("Rock won")
elif user1=="Paper" and user2=="Rock":
    print("Paper won")
elif user1=="Scissor" and user2=="Paper":
    print("Scissor won")
elif user1=="Rock" and user2=="Scissor":
    print("Rock won")
else:
    print("Invalid")


marks=int(input("Enter the marks:"))
name=input("Enter the name:")
if marks==600:
    print(name,"has got distinction with",marks,marks/600*100,"%")
elif marks>=520:
    print(name,"has got distinction with",marks,marks/600*100,"%")
elif marks>=420 and marks<=520:
    print(name,"has got first class with",marks,marks/600*100,"%")
elif marks>=320 and marks<=420:
    print(name,"has got second class with",marks,marks/600*100,"%")
else:print("Fail")
