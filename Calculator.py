def calculator(first,second):
    print("Please Choosen given in a options")
    userInput = input("Operand Selection \n 1)Addition \n 2)Subtraction \n"
                      " 3) Multiplication \n 4) Division")
    user = int(userInput)
    if user == 1:
        print(first+second)

    elif user == 2:
        print(first-second)

    elif user == 3:
        print(first*second)

    elif user == 4:
        print(first/second)
