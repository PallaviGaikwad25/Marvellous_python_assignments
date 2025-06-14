class Student:
    School_name="Army Public School,Pune"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def Display(self):
        print("Student Name",self.name)
        print("Student Roll number",self.roll_no)
        print("School Name",Student.School_name)

def main():
     
    print("enter the student information")
    sname=input()
    print("enter roll number of student ")
    sroll_no=int(input())
    obj1=Student(sname,sroll_no)
    obj1.Display()
    print("update school name")
    new_school_name=input()
    Student.School_name=new_school_name
    print("Updated information")
    obj1.Display()


if __name__=="__main__":
    main()