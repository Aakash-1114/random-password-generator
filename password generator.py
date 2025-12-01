

import string
import random

pass_len = int(input("Enter length of your password: "))

while True:
    print("\nPassword kis type ka chahiye?")
    print("1. Only Numbers")
    print("2. Only Alphabets")
    print("3. Numbers + Alphabets")
    print("4. Full Mixture (Alphabets + Numbers + Symbols)")

    choice = input("\nEnter your choice (1/2/3/4): ")

    if choice == "1":
        charValues = string.digits
        break

    elif choice == "2":
        charValues = string.ascii_letters
        break

    elif choice == "3":
        charValues = string.ascii_letters + string.digits
        break

    elif choice == "4":
        charValues = string.ascii_letters + string.digits + string.punctuation
        break

    else:
        print("\n Invalid choice! Please choose 1 to 4.\n")

password = "".join(random.choice(charValues) for _ in range(pass_len))

print("Your random password: ", password)
