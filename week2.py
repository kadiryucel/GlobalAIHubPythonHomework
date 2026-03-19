from datetime import datetime

name = input("Your name: ")
surname = input("Your surname: ")
age = int(input("Your age: "))
birth_year = int(input("Your birth year: "))

current_year = datetime.now().year
calculated_age = current_year - birth_year

print("-------------------------------------------------")

if calculated_age == age:
    print(f"Name: {name}")
    print(f"Surname: {surname}")
    print(f"Age: {age}")
    print(f"Birth year: {birth_year}")

    if age <= 18:
        print("You can't go out because it's too dangerous.")
    else:
        print("You can go out to the street.")
else:
    print("Your age and birth year do not match.")
    print("System is shutting down...")

print("-------------------------------------------------")