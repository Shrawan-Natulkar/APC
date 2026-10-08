status = input("Married? (yes/no): ")
gender = input("Gender (male/female): ")
age = int(input("Enter age: "))

if status.lower() == "yes":
    print("Driver is Insured")
elif status.lower() == "no" and gender.lower() == "male" and age > 30:
    print("Driver is Insured")
elif status.lower() == "no" and gender.lower() == "female" and age > 25:
    print("Driver is Insured")
else:
    print("Driver is Not Insured")