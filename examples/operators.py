is_student = True

# comparison to True with equality operator - not recommended
if is_student == True:
    print("1. Person is student.")

# comparison to True with `is` operator
if is_student is True:
    print("2. Person is student.")

# checks if is_student is ANY truthy value
if is_student:
    print("3. Person is student.")


age = None
age = age or 0

age = 0 if age is None else age  # ternary operator
# other languages:  cond ? val_if_true : val_if_false
# Python: val_if_true if cond else val_if_false
