while True:
    # Greatest among three numbers
    try:
        a, b, c = map(int, input("Enter three numbers with spaces: ").split())
        if (a > b) and (a > c):
            print(a, "is the greatest number")
        elif (b > a) and (b > c):
            print(b, "is the greatest number")
        else:
            print(c, "is the greatest number")
    except ValueError:
        print("Invalid input! Enter exactly three numbers.")

    print("Terminated\n")

    # Vowel or Consonant check
    ch = input("Enter a character (not capital): ").lower()
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")

    # Run again?
    again = input("\nDo you want to try again? (y/n): ")
    if again.lower() != 'y':
        print("Exiting program.")
        break
        