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
def letter_grades(grades): #use a variable to make it reusable
    for x in grades:#sort vs sorted - sorted creates new list in place of "x"
        if x < 60:
            f_index = grades.index(x)
            grades.remove(x)
            grades.insert(f_index, "F")
        elif 61 < x < 70:
            d_index = grades.index(x)
            grades.remove(x)
            grades.insert(d_index, "D")
        elif 71 < x < 80:
            c_index = grades.index(x)
            grades.remove(x)
            grades.insert(c_index, "C")
        elif 81 < x < 90:
            b_index = grades.index(x)
            grades.remove(x)
            grades.insert(b_index, "B")
        elif 91 < x < 100:
            a_index = grades.index(x)
            grades.remove(x)
            grades.insert(a_index, "A")
        else:
            print("Invalid grade please enter another")
    
    print(grades)

print(letter_grades(grades))