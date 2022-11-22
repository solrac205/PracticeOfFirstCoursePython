def validate_access(age_user):
    input_val = int(age_user)
    result = ""
    if (input_val < 18) and (input_val > 0):
        result = "Not Allowed Access"
    elif (input_val > 18) and (input_val < 100):
        result = "Allowed Access"
    elif input_val == 18:
        result = "Solicit Identification Document"
    else:
        result = "Invalid Age"
    return result


for x in range(4):
    evaluate_val = input("Enter User Age: ")
    print("The User is ", validate_access(evaluate_val))


# Finish Video 11
