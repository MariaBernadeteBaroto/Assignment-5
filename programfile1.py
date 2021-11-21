 # step 1. Ask for grade percentage, covet and store

grade = float(input("What is your grade percentage? "))
 
# grade/mark    percentage     description
# 1.0           97-100          Excellent
if grade >= 96.5 and grade <= 100:
    print("mark: 1.0")
    print("description: Excellent")
# 1.25          94-96           Excellent
elif grade >= 93.5 and grade <= 96.4:
    print("mark: 1.25") 
    print("description: Excellent")
# 1.5           91-93           Very Good
elif grade >= 90.5 and grade <= 93.4:
    print("mark: 1.5")
    print("description: Very Good")
# 1.75          88-90           Very Good
elif grade >= 87.5 and grade <= 90.4:
    print("mark: 1.75")
    print("description: Very Good")
# 2.0           85-87           Good
elif grade >= 84.5 and grade <= 87.4:
    print("mark: 2.0")
    print("description: Good")
# 2.25          82-84           Good
elif grade >= 81.5 and grade <= 84.4:
    print("mark: 2.25")
    print("description: Good")
# 2.50          79-81           Satisfactory
elif grade >= 78.5 and grade <= 81.4:
    print("mark: 2.50")
    print("description: Satisfactory")
# 2.75          76-78           Satisfactory
elif grade >= 75.5 and grade <= 78.4:
    print("mark: 2.75")
    print("description: Satisfactory")
# 3.0           75              Passing
elif grade == 75:
    print("mark: 3.0")
    print("description: passing")
# 5.0           65-74           Failure
elif grade >= 64.5 and grade <= 74.4:
    print("mark: 5.0")
    print("description: Failure")
else:
    if grade == 0:
        print(" You are Incomplete, Withdrawn or Dropped")


print("DONE!")


                    