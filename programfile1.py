 # step 1. Ask for grade percentage, covet and store

grade = int(input("What is your grade percentage? "))
 
# grade/mark    percentage     description
# 1.0           97-100          Excellent
if grade >= 97 and grade <= 100:
    print("mark: 1.0")
    print("description: Excellent")
else:
   # 1.25          94-96           Excellent 
   if grade >= 94 and grade<= 96:
       print("mark: 1.25")
       print("description: Excellent")
       
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.50          79-81           Satisfactory
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropeed