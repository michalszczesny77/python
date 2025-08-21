import numpy as np

grades = np.random.randint(1,7, size=20)
grade_counts = np.bincount(grades, minlength=7)
for grade, num in enumerate(grade_counts[1:], start=1):
    print(f"Grade {grade}: {num} students")

above_avg = grades[grades > np.mean(grades)]
below_avg = grades[grades < np.mean(grades)]
passed = np.sum(grades >= 3) / len(grades) * 100

print(f"Average grade: {np.mean(grades):.1f}")
print(f"Median grade: {np.median(grades)}")
print(f"Best grade: {np.max(grades)}")
print(f"Worst grade: {np.min(grades)}")
print(f"Students above average: {np.sort(above_avg)}")
print(f"Students below average: {np.sort(below_avg)}")
print(f"{passed:.0f}% students passed the exam!")