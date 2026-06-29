name = input("Enter Student Name:raj ")

m1 = int(input("Enter Marks of Subject 1: "))
m2 = int(input("Enter Marks of Subject 2: "))
m3 = int(input("Enter Marks of Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 95:
    print("Grade: A+")
elif percentage >= 75:
    print("Grade: A")
elif percentage >= 50:
    print("Grade: B")
elif percentage >= 35:
    print("Grade: C")
else:
    print("Grade: Fail")