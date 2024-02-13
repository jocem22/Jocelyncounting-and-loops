for i in range(99, 0, -1):
    print(f"{i} bottles of beer on the wall")
    print(f"{i} bottles of beer")
    print("Take one down, pass it around")

    if i == 6:
        print(f"If one of those bottles should happen to fall, {i-1} bottles of beer on the wall...\n")
    elif i > 1:
        print(f"{i-1} bottles of beer on the wall\n")
    else:
        print("No more bottles of beer on the wall\n")
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("We've taken them down and passed them around;")
        print("Now we're drunk and passed out!")