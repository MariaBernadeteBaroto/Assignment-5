# step
# 1. ask for age, covet and store
age = int(input("Age: "))

# 2. test if kid
if age > -1 and age <= 12:
    print("kid") # true block
else: 
    # 3. test if teen
    if age>= 13 and age <=17:
        print("Teen")  # true block
    else:
        # 4. test if debut
        if age == 18:
            print("Debut")
        else:
            # 5. sure adult
            print("Adult")

print("Done!")



