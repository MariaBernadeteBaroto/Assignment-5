 # step 1. Ask for grade percentage, covet and store

grade = int(input("What is your grade percentage? "))
 
# grade/mark    percentage     description
# 1.0           97-100          Excellent
if grade >= 97 and grade <= 100:
    print("mark: 1.0")
    print("description: Excellent")
else:
    # 1.25          94-96           Excellent
    if grade >= 94 and grade <= 96:
        print("mark: 1.25") 
        print("description: Excellent")
    else:
        # 1.5           91-93           Very Good
        if grade >= 91 and grade <= 93:
            print("mark: 1.5")
            print("description: Very Good")
        else:
            # 1.75          88-90           Very Good
            if grade >= 88 and grade <= 90:
                print("mark: 1.75")
                print("description: Very Good")
            else:
                # 2.0           85-87           Good
                if grade >= 85 and grade <= 87:
                    print("mark: 2.0")
                    print("description: Good")
                else:
                    # 2.25          82-84           Good
                    if grade >= 82 and grade <= 84:
                        print("mark: 2.25")
                        print("description: Good")
                    else:
                        # 2.50          79-81           Satisfactory
                        if grade >= 79 and grade <= 81:
                            print("mark: 2.50")
                            print("description: Satisfactory")
                        else:
                            # 2.75          76-78           Satisfactory
                            if grade >= 76 and grade <= 78:
                                print("mark: 2.75")
                                print("description: Satisfactory")
                            else:
                                # 3.0           75              Passing
                                if grade == 75:
                                    print("mark: 3.0")
                                    print("description: passing")
                                else:
                                    if grade >= 65 and grade <= 74:
                                        print("mark: 5.0")
                                        print("description: Failure")
                                    
                        
                


# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropeed