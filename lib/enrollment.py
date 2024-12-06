class Enrollment:
    # Class to represent an Enrollment
    all = []  # This will hold all the enrollments

    def __init__(self, student, course, enrollment_date):
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date
        self.__class__.all.append(self)  # Add this enrollment to the global list

    def get_enrollment_date(self):
        return self.enrollment_date


class Course:
    # Class to represent a Course
    def __init__(self, course_name):
        self.course_name = course_name
        self._enrollments = []

    def add_enrollment(self, enrollment):
        self._enrollments.append(enrollment)

    @classmethod
    def aggregate_enrollments_per_day(cls):
        # Count enrollments per day
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()  # Get the date part of the enrollment date
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count

    def total_students(self):
        # Returns the total number of students enrolled in this course
        return len(self._enrollments)


class Student:
    # Class to represent a Student
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}  # Mapping of enrollment to grades

    def enroll(self, enrollment):
        self._enrollments.append(enrollment)

    def add_grade(self, enrollment, grade):
        self._grades[enrollment] = grade

    def course_count(self):
        # Count the number of courses the student is enrolled in
        return len(self._enrollments)

    def aggregate_average_grade(self):
        # Calculate the average grade for the student
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        if num_courses > 0:
            average_grade = total_grades / num_courses
        else:
            average_grade = 0  # Avoid division by zero if no grades
        return average_grade
