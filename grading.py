

def calculate_grade(math, geo, phic, chem):
    if math <= 0 or geo <= 0 or phic <= 0 or chem <= 0:
        print("Invalid entry. Marks cannot be zero or negative.")
        return
    if math> 100 or geo> 100 or phic> 100 or chem> 100:
        print("Invalid entry. Marks cannot be greater than 100.Check your entries again")
        return
    average = (math + geo + phic + chem) / 4

    if 71 <= average <= 100:
        grade = 'A'
    elif 51 <= average <= 70:
        grade = 'B'
    elif 31 <= average <= 50:
        grade = 'C'
    elif 0 <= average <= 30:
        grade = 'D'
    else:
        print("Invalid average calculation. Please check your marks.")
        return

    print(f"Your average is {average:.2f}, and your grade is {grade}.")


math = float(input("Enter marks for Maths: "))
geo = float(input("Enter marks for Geography: "))
phic = float(input("Enter marks for Phisycs: "))
chem = float(input("Enter marks for Chemistry: "))

calculate_grade(math, geo, phic, chem)
