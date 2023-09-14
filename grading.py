grade = int(input("Enter a number you would like to imput:"))

if grade > 80 and grade <= 100:
    print("Congratulations you scored a A")
elif grade > 60 and grade <= 80:
    print("Congratulations you scored a B+")
elif grade > 40 and grade <= 60:
    print("Congratulations you scored a B")
else:
    print("You have Failed the test ,need a retake!!")