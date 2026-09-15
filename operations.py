import sqlite3
import validators 
from student import Student
def formatted_output() :
    print("=" * 48)
    print(f"{'Roll No':<10}{'Name':<15}{'Age':<10}{'Marks':<10}{'Result':<15}")
    print("=" * 48)
def initialize_database() :
    conn = sqlite3.connect("Students_Data.db")
    conn.execute("""
    create table if not exists Students(
        NAME text not null ,
        ROLL_NO integer primary key,
        AGE integer not null,
        MARKS float
    )
    """)
    conn.commit()
    conn.close()
def add_student():
    name = validators.get_valid_name()
    age = validators.get_valid_age()
    marks = validators.get_valid_marks()
    conn = sqlite3.connect("Students_Data.db")
    conn.execute("""
    insert into Students (NAME,AGE,MARKS)
    values (?,?,?)
    """,(name,age,marks)
    )
    conn.commit()
    conn.close()
    print("Student added successfully.")
def search_student() :
    print("1. Search by name.")
    print("2. Search by roll no.")
    while True :
        try :
            choose = int(input("Enter the choice :"))
            break
        except ValueError :
            print("Invalid Choice.Choose an integer.")
    if choose == 1 :
        search = input("Enter the name of student : ")
        search = search.title()
        found = False
        conn = sqlite3.connect("Students_Data.db")
        cursor = conn.execute("SELECT * FROM Students WHERE NAME = ?",(search,))
        formatted_output()
        for row in cursor :
            student = Student(row[0], row[1], row[2], row[3])
            print(f"{row[1]:<10}{row[0]:<15}{row[2]:<10}{row[3]:<10}{student.get_result():<15}")
            found=True
        if(not found) :
            print("Student not found.")
        conn.close()
    elif choose == 2 : 
        while True :
            try :
                search = int(input("Enter the roll no : "))
                break
            except ValueError :
                print("Enter the valid Roll number.")
        conn = sqlite3.connect("Students_Data.db")
        cursor = conn.execute("SELECT * FROM Students WHERE ROLL_NO = ?",(search,))
        row = cursor.fetchone()
        if row is None :
            print("Student not found.")
        else :
            student = Student(row[0], row[1], row[2], row[3])
            formatted_output()
            print(f"{row[1]:<10}{row[0]:<15}{row[2]:<10}{row[3]:<10}{student.get_result():<15}")
        conn.close()
    else :
        print("Invalid Integer.Choose from given choices.")
def delete_student(): 
    while True :
        try :
            delete = int(input("Enter the roll no of student : "))
            break
        except ValueError :
            print("Enter a valid roll number.")
    conn = sqlite3.connect("Students_Data.db")
    cursor = conn.execute("DELETE FROM Students WHERE ROLL_NO = ? ",(delete,))
    if cursor.rowcount == 1 :
        print("Deleted Successfully")
    else :
        print("Nothing matches your search")
    conn.commit()
    conn.close()
def display_students():
    conn = sqlite3.connect("Students_Data.db")
    table_entries = conn.execute("SELECT * FROM Students")
    found = False
    formatted_output()
    for row in table_entries :
        student = Student(row[0], row[1], row[2], row[3])
        print(f"{row[1]:<10}{row[0]:<15}{row[2]:<10}{row[3]:<10}{student.get_result():<15}")
        found = True
    if not found :
        print("No student added.")
    conn.close()

def update_student():
    while True :
        try :
            roll_no = int(input("Enter roll no to update: "))
            break
        except ValueError :
            print("You entered an invalid roll number.")
    
    conn = sqlite3.connect("Students_Data.db")
    cursor = conn.execute(
    "SELECT * FROM Students WHERE ROLL_NO = ?",
    (roll_no,)
)
    row = cursor.fetchone()
    if row is None :
        print("No student found.")
        conn.close()
    else :
        s = Student("",roll_no,0,0)
        s.set_age(validators.get_valid_age()) 
        s.set_name(validators.get_valid_name())
        s.set_marks(validators.get_valid_marks())
        cursor = conn.execute("UPDATE Students SET NAME = ?,AGE =?,MARKS = ? WHERE ROLL_NO = ?",(s.get_name(),s.get_age(),s.get_marks(),roll_no,))
        conn.commit()
        conn.close()        