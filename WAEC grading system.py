students = int(input("How many students do you have?"))
for ahuma in range(students):
    print(f"\nEntering details for student {ahuma + 1}:")
    name = str(input("Name: "))
    score = int(input("Score: "))
    if score <0 or score >100:
        print("unable to access student")
    elif score >= 80:
        print("grade A, keep it up")
    elif score >= 70:
        print("grade B, keep it up")
    elif score >= 60:
        print("grade C, keep going")
    elif score >= 50:
        print("grade D, get up and start again")
    elif score >= 40:
        print("grade E, work on yourself for improvement")
    elif score <= 40:
        print("grade F, there is the need for serious improvement")
        print(students)
