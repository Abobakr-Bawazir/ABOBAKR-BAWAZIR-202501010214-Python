choice = "y"

while choice == "y":

    # Get quiz marks from user
    quiz_1 = int(input("Enter Quiz 1 mark: "))
    quiz_2 = int(input("Enter Quiz 2 mark: "))
    quiz_3 = int(input("Enter Quiz 3 mark: "))

    # Calculate average
    average = (quiz_1 + quiz_2 + quiz_3) / 3

    # Display average
    print("Average =", average)

    # Check pass or fail
    if average >= 50:
        print("Pass")
    else:
        print("Fail")

    # Ask user to continue
    choice = input("Continue? Select Y/N: ").lower()

print("Program Ended")