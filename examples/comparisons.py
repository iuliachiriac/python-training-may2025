temp = None
if temp is None:  # comparison with None should be done with `is` operator
    print("Temperature not defined.")

is_student = True
if is_student:  # any truthy value
    print("Person is student")

if is_student is True:  # comparison with True
    print("Yes, a student.")


age = 10
# age = None
print(age if age is not None else 0)  # ternary operator
print(age or 0)
