student_name = "Kadir YUCEL"

courses = [
    "Linear Algebra",
    "Introduction to Engineering",
    "Physics",
    "Calculus",
    "Statistics",
    "Algebra",
    "Robotics",
    "Introduction to Electronics",
    "Machine Learning",
    "Artificial Intelligence"
]

for attempt in range(3):
    full_name = input("Enter your name and surname:\n")

    if full_name == student_name:
        print(f"Welcome, {student_name}!")
        print("\nAvailable courses:")
        
        for course in courses:
            print("-", course)

        print("\nINFORMATION: You must choose at least 3 and at most 5 courses.")
        course_count = int(input("How many courses do you want to choose?\n"))

        if course_count < 3 or course_count > 5:
            print("You did not choose the required number of courses. You failed the class...")
            break

        selected_courses = []

        for i in range(course_count):
            selected_course = input(f"{i + 1}) Enter course name: ")
            selected_courses.append(selected_course)
            print(f"Selected course: {selected_course}")

        chosen_course = input("\nChoose one of the courses you selected above:\n")

        print("Enter your midterm, final, and project grades below.")
        midterm = float(input("Enter your midterm grade: "))
        final = float(input("Enter your final grade: "))
        project = float(input("Enter your project grade: "))

        average = (midterm * 0.30) + (final * 0.50) + (project * 0.20)

        if average >= 90:
            print(f"Your average: {average}\nYour grade: AA\nYou passed the class.")
        elif 70 <= average < 90:
            print(f"Your average: {average}\nYour grade: BB\nYou passed the class.")
        elif 50 <= average < 70:
            print(f"Your average: {average}\nYour grade: CC\nYou passed the class.")
        elif 30 <= average < 50:
            print(f"Your average: {average}\nYour grade: DD\nYou passed the class.")
        else:
            print(f"Your average: {average}\nYour grade: FF\nYou failed the class.")

        break

    else:
        print("You entered your name or surname incorrectly. Please try again.")