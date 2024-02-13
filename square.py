count = input("How big of a square do you want? Enter a number: ")

for _ in range(int(count)):
    for _ in range(int(count)):
        print("*", end="")
    print("")