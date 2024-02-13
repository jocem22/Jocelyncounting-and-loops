count = input("What size of backward triangle do you want? Enter a number: ")
count2 = int(count)

for num in range(1, count2 + 1):
    # Print leading spaces
    for _ in range(count2 - num):
        print(" ", end="")
    
    # Print asterisks
    print("*" * num)