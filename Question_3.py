#Task 1
students = ['John', 'Sarah', 'Sam', 'Melissa', 'James']

grades = [99, 67, 54, 84, 77]

def average_grade():
    total_grade = sum(grades)
    return total_grade/len(students)

print(f"Class average: {average_grade()}")

#Task 2
def max_grade():
    return max(grades)

print(f"Highest grade in the class: {max_grade()}")

def min_grade():
    return min(grades)

print(f"Lowest grade in the class: {min_grade()}")

#Task 3
def letter_grades():
    for x in grades:
        if x < 50:
            print(f"{students[len[x]]} has an f")

print(letter_grades())