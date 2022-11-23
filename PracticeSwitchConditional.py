# The "switch" conditional is a structure for multiple conditions,
# and python does not have this structure.
# In equivalent in python have the concatenation of comparison operators.

def valid_age(age_validate):
    if 0 < age < 100:
        print("The Age is correct.")
    else:
        print("The age is not correct.")


age = -10
valid_age(age)
age = 30
valid_age(age)
age = 150
valid_age(age)


def salaries_validation(salaries):
    if salaries[0] < salaries[1] < salaries[2] < salaries[3]:
        print("All salaries assigned are correct.")
        print(f'President: $. {salaries[3]:,.2f}')
        print(f'Director: $. {salaries[2]:,.2f}')
        print(f'Area Chief: $. {salaries[1]:,.2f}')
        print(f'Administrative: $. {salaries[0]:,.2f}')

    else:
        print("Exist error in salaries assigned.")


print("****************************************************")
print("Salaries Validation")
print("****************************************************")
president_salary = float(input("Enter Salary of president: "))
director_salary = float(input("Enter salary of director: "))
area_chief_salary = float(input("Enter salary of area chief: "))
administrative_salary = float(input("Enter salary of administrative: "))
salaries_values = [administrative_salary, area_chief_salary, director_salary, president_salary]
salaries_validation(salaries_values)

# Finish video 12

# The practice of Operators "and" and "or"
# Case the evaluation of if a student is a candidate to benefit from a scholarship
# Factors:
# Distance they live >40klm
# Number of siblings > 2
# Family salary <= $ 20000


def evaluate_scholarship_candidate(distance, siblings, salary):
    if (distance > 40) and \
       (siblings > 2) and \
       (salary <= float(20000)):
        print("Candidate for a scholarship...")
    else:
        print("Does not is a Candidate for a scholarship...")


print("Program of scholarships 2022")
distance_they_live = int(input("Distance they live in Kilometers: "))
siblings_number = int(input("Siblings number: "))
family_salary = float(input("family salary: "))
evaluate_scholarship_candidate(distance_they_live, siblings_number, family_salary)


def evaluate_scholarship_candidate_flexible(distance, siblings, salary):
    if ((distance > 40) and
       (siblings > 2)) or \
       (salary <= float(20000)):
        print("Candidate for a scholarship...")
    else:
        print("Does not is a Candidate for a scholarship...")


print("Program of scholarships 2022")
distance_they_live = int(input("Distance they live in Kilometers: "))
siblings_number = int(input("Siblings number: "))
family_salary = float(input("family salary: "))
evaluate_scholarship_candidate_flexible(distance_they_live, siblings_number, family_salary)


# "in" operator use

print("Optional Courses year 2022")
list_courses = ["math", "sports", "languages", "logic"]
print(f"Choice a course from the list: ", ", ".join(str(x).capitalize() for x in list_courses))

course_selected = input("Name course selected: ")
if course_selected.lower() in list_courses:
    print("Course is assigned successful.")
else:
    print("Course not exists in list")

# Finish video 13
