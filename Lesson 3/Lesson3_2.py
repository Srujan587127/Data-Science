import pandas as pd

student_data = {
    "Student": ["John", "Sarah", "Micheal", "Emma", "David"],
    "Math Marks": [85,92,76,88,95],
    "Science Marks": [78,85,90,65,82],
    "English Marks": [80,75,65,78,92]

}

df = pd.DataFrame(student_data)

print("Student Marks Dataset")
print(df)

max_math = df["Math Marks"].max()

highest_math = df[df["Math Marks"] == max_math]

print("\nStudent with the Highest math marks:")
print(highest_math[["Student", "Math Marks"]])

min_science = df["Science Marks"].min()

lowest_science = df[df["Science Marks"] == min_science]

print("\nStudent with the lowest science marks:")
print(lowest_science[["Student", "Science Marks"]])

avg_english = df["English Marks"].mean()

print("\nAverage English Marks:", avg_english)

students_above_80 = df[df["Math Marks"] > 80]

print("\nStudents with Math Marks Greater than 80:")
print(students_above_80[["Student", "Math Marks"]])