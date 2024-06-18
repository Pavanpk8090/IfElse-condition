num1=input("Enter the number:")
num2=input("Enter the number:")
num3=input("Enter the number:")
if num1 is num2 is num3:
    print("Equilateral triangle")
elif num1 is num2 or num2 is num3 or num1 is num3:
    print("Isoceleus triangle")
else:
    print("Scalene triangle")