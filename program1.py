# step 1. Ask for Grade Percentage, covet and store
grade = int(input("What is your grade percentage?: "))

# grade/mark    percentage     description

# 1.0           97-100          Excellent
if grade >= 97 and grade <= 100:
    print("mark: 1.o")
    print("Description: Excellent")

# 1.25          94-96           Excellent
elif grade >= 94 and grade <= 96:
    print("mark: 1.25")
    print("Description: Excellent ")

# 1.5           91-93           Very Good
elif grade >= 91 and grade <= 93:
    print("mark: 1.5")
    print("Description: very good")

# 1.75          88-90           Very Good
elif grade >= 88 and grade <= 90:
    print("mark: 1.75")
    print("Description: Very good")

# 2.0           85-87           Good
elif grade >= 85 and grade <= 87:
    print("mark: 2.0")
    print("Description: good")

# 2.25          82-84           Good
elif grade >= 82 and grade <= 84:
    print("mark: 2.25")
    print("Description: Good")
# 2.50          79-81           Satisfactory
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropeed