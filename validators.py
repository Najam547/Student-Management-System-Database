def get_valid_name() :
    while True :
        name = input("Enter your name : ")
        if name.replace(" ","").isalpha() :
            break
        else :
            print("Invalid Name.Please use alphabets only.")
    name = name.title()
    return name
def get_valid_age():
    while True :
        try :
            age = int(input("Enter age: "))
            break
        except ValueError:
            print("Invalid input.Try again.")
    while age < 3 or age > 22 :
        age = int(input("Enter valid age: "))
    return age

def get_valid_marks():
    while True :
        try :
            marks = float(input("Enter marks: "))
            break
        except ValueError:
            print("Enter valid marks.")
    while marks < 0 or marks > 100:
        marks = float(input("Enter valid marks: "))
    return marks