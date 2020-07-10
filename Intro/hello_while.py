counter = 0

while counter < 10:
    print(f"Still counting! {counter}")
    if counter == 6:
        break
    counter += 1

print("We've escaped the while loop")

age = ""
while not age.isnumeric():
    age = input("Enter your age:\n")
    if not age.isnumeric():
       print("That's not a number, try again")

age = int(age)
print("You are " + str(age))