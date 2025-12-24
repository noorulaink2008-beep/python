print("===== STUDENT GRADE MANAGEMENT SYSTEM =====")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

while True:
    try:
        subjects_count = int(input("Enter number of subjects: "))
        if subjects_count <= 0:
            print("Please enter a positive number!")
            continue
        break
    except:
        print("Invalid input! Please enter a number.")

subjects = []
total_marks = 0
obtained_marks = 0

for i in range(subjects_count):
    print("\n--- Subject", i+1, "---")

    while True:
        sub_name = input("Enter Subject Name: ")
        if sub_name.replace(" ", "").isalpha():  # checks letters only
            break
        else:
            print("Invalid subject name! Only alphabets allowed.")

    
    while True:
        try:
            sub_total = float(input("Enter Total Marks: "))
            if sub_total <= 0:
                print("Marks must be greater than zero!")
                continue
            break
        except:
            print("Invalid input! Please enter a number.")

    
    while True:
        try:
            sub_obtained = float(input("Enter Obtained Marks: "))
            if sub_obtained < 0 or sub_obtained > sub_total:
                print("Obtained marks must be between 0 and total marks!")
                continue
            break
        except:
            print("Invalid input! Please enter a number.")

    subjects.append([sub_name, sub_total, sub_obtained])

    total_marks += sub_total
    obtained_marks += sub_obtained

percentage = (obtained_marks / total_marks) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== RESULT SUMMARY =====")
print("Name:", name)
print("Roll No:", roll)

print("\nSubject-wise Marks:")
for s in subjects:
    print(s[0], ":", s[2], "/", s[1])

print("\nTotal Marks Obtained:", obtained_marks, "/", total_marks)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

choice = input("\nDo you want to save result in a text file? (yes/no): ")

if choice.lower() == "yes":
    filename = roll + "_result.txt"
    f = open(filename, "w")
    f.write("Student Name: " + name + "\n")
    f.write("Roll Number: " + roll + "\n\n")
    f.write("Subject-wise Marks:\n")
    for s in subjects:
        f.write(f"{s[0]} : {s[2]} / {s[1]}\n")

    f.write("\nTotal Marks Obtained: " + str(obtained_marks) + "/" + str(total_marks))
    f.write("\nPercentage: " + str(round(percentage, 2)) + "%")
    f.write("\nGrade: " + grade)
    f.close()
    print("Result saved in file:", filename)

print("\n===== PROGRAM END =====")
