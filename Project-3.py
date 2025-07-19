pressence = int(input("Enter total of the days you were present :"))

if pressence == 75:
    print("You are allowed to sit for the exam")

elif pressence > 75:
    print("You are allowed to sit for the exam")

else:
    print("You are not allowed to sit for the exam")

    absence = input("Do you have a valid reason for your absence?")
    
    if absence == "yes":
        print("Then you can sit for the exam")

    elif absence == "no":
        print("Then sorry, but you are still not allowed to sit for the exam")