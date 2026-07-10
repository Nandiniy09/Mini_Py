# College Placement Management System

class Placement:

    def __init__(self):
        self.students = []
        self.companies = []


    def add_student(self):

        print("\n===== Add Student Details =====\n")

        name = input("Student Name: ")
        course = input("Course: ")
        cgpa = float(input("CGPA: "))
        skills = input("Skills: ")

        student = {
            "Name": name,
            "Course": course,
            "CGPA": cgpa,
            "Skills": skills,
            "Status": "Not Selected"
        }

        self.students.append(student)

        print("\nStudent Added Successfully ✅")


    def add_company(self):

        print("\n===== Add Company Details =====\n")

        name = input("Company Name: ")
        required_cgpa = float(input("Required CGPA: "))

        company = {
            "Name": name,
            "Required CGPA": required_cgpa
        }

        self.companies.append(company)

        print("\nCompany Added Successfully ✅")


    def check_eligibility(self):

        print("\n===== Eligibility Result =====")

        for company in self.companies:

            print("\nCompany:", company["Name"])

            for student in self.students:

                print("\nStudent:", student["Name"])
                print("CGPA:", student["CGPA"])

                if student["CGPA"] >= company["Required CGPA"]:

                    print("Result: Eligible ✅")
                    student["Status"] = "Selected 🎉"

                else:

                    print("Result: Not Eligible ❌")


    def placement_report(self):

        print("\n===== Placement Report =====")

        for student in self.students:

            print("\nName:", student["Name"])
            print("Course:", student["Course"])
            print("CGPA:", student["CGPA"])
            print("Skills:", student["Skills"])
            print("Status:", student["Status"])



# Object Creation

system = Placement()


# Adding Multiple Students

number = int(input("Enter Number of Students: "))

for i in range(number):
    system.add_student()


# Adding Multiple Companies

company_number = int(input("\nEnter Number of Companies: "))

for i in range(company_number):
    system.add_company()


# Checking Eligibility

system.check_eligibility()


# Display Placement Report

system.placement_report()