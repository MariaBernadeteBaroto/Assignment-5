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
elif grade >= 79 and grade <= 81:
    print("mark: 2.50")
    print("description: satisfactory")

# 2.75          76-78           Satisfactory
elif grade >= 76 and grade <= 78:
    print("mark: 2.75")
    print("description: satisfactory")

# 3.0           75              Passing
elif grade == 75:
    print("mark: 3.0")
    print("description: passing")

# 5.0           65-74           Failure
elif grade >= 65 and grade <= 74:
    print("mark: 5.0")
    print("description: failure")
    
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropeed