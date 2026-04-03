"""
Student: Sameer Ahadi
Course: CSC-101
Date: 11/23/2025
Description: Student Managment System
"""


class Course:
    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits

    def __str__(self):
        return f"{self.code} - {self.name} ({self.credits} credits)"


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course.name}")
        else:
            print(f"{self.name} is already enrolled in {course.name}")

    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{self.name} dropped {course.name}")
        else:
            print(f"{self.name} is not enrolled in {course.name}")

    def display_info(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Enrolled Courses:")
        if not self.courses:
            print("  - None")
        else:
            for c in self.courses:
                print(f"  - {c}")


def main():

    #Creating 3 course objects
    intro_python = Course("Intro to Python", "CSC110", 3)
    calculus = Course("Calculus I", "MATH101", 4)
    history = Course("World History", "HIST201", 3)

    #Creating 2 student objects
    alice = Student("Alice Johnson", "S12345")
    bob = Student("Bob Martinez", "S67890")

    #Enrolling each student in at least 2 courses
    alice.enroll(intro_python)
    alice.enroll(calculus)

    bob.enroll(calculus)
    bob.enroll(history)

    #Display information before dropping
    alice.display_info()
    bob.display_info()

    #Drop a course and display information after dropping
    alice.drop(calculus)
    alice.display_info()


if __name__ == "__main__":
    main()
