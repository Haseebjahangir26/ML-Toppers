def average():
    average_all = (English_marks + urdu_marks + math_marks)/3
    return average_all
    

name = input("Enter your Name : ")
age = int(input("Enter your age : "))

English_marks = int(input("Enter marks for subject english "))

math_marks = int(input("Enter marks for subject math "))

urdu_marks = int(input("Enter marks for subject urdu "))

marks = {"English" : English_marks , "Math" : math_marks, "urdu" : urdu_marks}
    
bonus = input("Do you want to give extra marks to the student ? Reply with y or n")

if (bonus == "y"):
    English_marks = English_marks+ 5
    urdu_marks = urdu_marks + 5
    math_marks = math_marks +5
else:
    print("no bonus marks given")
total_average = average()
grade_english = 0
if (English_marks >= 80):
    print("student has A grade in english")
    grade_english = "A"
elif(English_marks>= 60 and English_marks<=79):
    print("student has B grade in english")
    grade_english = "B"
elif(English_marks>= 40 and English_marks<=59):
    print("student has C grade in english")
    grade_english = "C"
else:
    print("student has F grade in english")
    grade_english = "F"
    
grade_math = 0
if (math_marks >= 80):
    print("student has A grade in math")
    grade_math = "A"
elif(math_marks>= 60 and math_marks<=79):
    print("student has B grade in math")
    grade_math = "B"
elif(math_marks>= 40 and math_marks<=59):
    print("student has C grade in math")
    grade_math = "C"
else:
    print("student has F grade in math")
    grade_math = "F"
    
grade_urdu = 0
if (urdu_marks >= 80):
    print("student has A grade in urdu")
    grade_urdu = "A"
elif(urdu_marks>= 60 and urdu_marks<=79):
    print("student has B grade in urdu")
    grade_urdu = "B"
elif(urdu_marks>= 40 and urdu_marks<=59):
    print("student has C grade in urdu")
    grade_urdu = "C"
else:
    print("student has F grade in urdu")
    grade_urdu = "F"

print("the final report of the student is given below")
print("Name:" , name)
print("Age" , age)
print("Math: ", math_marks)
print("English: ", English_marks)
print("urdu: ", urdu_marks)
print("average: ", total_average)
