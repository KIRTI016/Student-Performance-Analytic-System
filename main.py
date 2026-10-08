import pandas as pd
import numpy as np
df = pd.read_csv("students.csv")

print("========STUDENT DATA =========")
print(df)
print("\nNumber of Students:", len(df))
print("Columns:", list(df.columns))
def find_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"
subjects = ["Python", "DBMS", "DSA", "OS", "JavaScript"]

passed = 0
failed = 0
averages = []

print("\n========== STUDENT PERFORMANCE ==========")
for i in range(len(df)):

    marks = [
        df["Python"][i],
        df["DBMS"][i],
        df["DSA"][i],
        df["OS"][i],
        df["JavaScript"][i]
    ]

    total = np.sum(marks)
    average = np.mean(marks)

    averages.append(average)

    grade = find_grade(average)

    if average >= 40:
        result = "Pass"
        passed += 1
    else:
        result = "Fail"
        failed += 1

    print("\nName:", df["Name"][i])
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("Attendance:", df["Attendance"][i])
    print("Result:", result)
print("\n========== SUBJECT-WISE AVERAGE ==========")
subject_averages = []
for subject in subjects:
    avg = np.mean(df[subject])
    subject_averages.append(avg)
    print(subject, ":", round(avg, 2))
highest_average = max(averages)
lowest_average = min(averages)
class_average = np.mean(averages)

highest_student = df["Name"][averages.index(highest_average)]
lowest_student = df["Name"][averages.index(lowest_average)]

best_subject = subjects[subject_averages.index(max(subject_averages))]

print("\n========== CLASS ANALYSIS ==========")

print("Students Passed:", passed)
print("Students Failed:", failed)
print("Highest Average:", round(highest_average, 2))
print("Highest Average Student:", highest_student)
print("Lowest Average:", round(lowest_average, 2))
print("Lowest Average Student:", lowest_student)
print("Class Average:", round(class_average, 2))
print("Best Subject:", best_subject)
print("\n========== TOP PERFORMER ==========")
print("Name:", highest_student)
print("Average:", round(highest_average, 2))
print("Grade:", find_grade(highest_average))