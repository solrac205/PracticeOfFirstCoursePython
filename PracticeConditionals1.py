# Conditionals If
# The command "if" is a structure that breaks a program flow if the condition is met,
# and the finish of the contained returns to the normal flow of the program.
#
# If the condition not is met, this instruction does not break the normal program flow.

def evaluation(note):
    if note >= 60:
        print("Student is approved..")
    else:
        print("Student is not approved..")


evaluation(50)

evaluation(70)


def student_approved(note):
    result = "Approved"
    if note < 60:
        result = "Not Approved"
    return result


print("The Student is: ", student_approved(70))

print("The Student is: ", student_approved(50))


def student_validate(note):
    input_val = int(note)
    result = "Approved"
    if input_val < 60:
        result = "Not Approved"
    return result


for x in range(2):
    evaluate_val = input("Enter Note: ")
    print("The Student is: ", student_validate(evaluate_val))

# The variables are accessible in a context or ambit

# Finish Video 10
