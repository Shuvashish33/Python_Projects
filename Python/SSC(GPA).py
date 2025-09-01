print("Enter your grade score (0-5)")
B = float(input("Bangla = "))
E = float(input("English = "))
M = float(input("General Math = "))
BGS = float(input("Bangladesh and Global Studies = "))
R = float(input("Religious Studies = "))
P = float(input("Physics = "))
C = float(input("Chemistry = "))
Bio = float(input("Biology = "))
I = float(input("ICT = "))
H1 = float(input("Higher Math = "))

# Optional subject adjustment
H = H1 - 2

# Check for fail in any compulsory subject
if (B * E * M * BGS * R * I * P * C * Bio) == 0:
    print("\n\nresult=F")
    print("Comments:Don't demotivate, you can\nstill bounce back, so keep hardworking.")
else:
    GPA = (B + E + M + BGS + R + I + P + C + Bio + H) / 9
    
    if GPA >= 5:
        print("\n\nTotal GPA=5")
    else:
        print("\nTotal GPA =", round(GPA, 2))
    
    # Grade calculation
    if GPA >= 5:
        print("Grade = A+")
        grade = 'X'  # Custom char for A+
    elif GPA >= 4:
        print("Grade = A")
        grade = 'A'
    elif GPA >= 3.5:
        print("Grade = A-")
        grade = 'Y'  # Custom char for A-
    elif GPA >= 3:
        print("Grade = B")
        grade = 'B'
    elif GPA >= 2:
        print("Grade = C")
        grade = 'C'
    elif GPA >= 1:
        print("Grade = D")
        grade = 'D'
    else:
        print("Grade = F")
        grade = 'F'

    # Comments based on grade
    if grade == 'X':
        print("Comments:Excellent!")
    elif grade == 'A':
        print("Comments:Very good!")
    elif grade == 'Y':
        print("Comments:Good job!")
    elif grade == 'B':
        print("Comments:Keep studying.")
    elif grade == 'C':
        print("Comments:You need to study more.")
    elif grade == 'D':
        print("Comments:Very poor performance,\ngo and study right now")
    elif grade == 'F':
        print("Comments:Don't demotivate, you can\nstill bounce back, so keep hardworking.")
    else:
        print("Comments:Invalid grade.")