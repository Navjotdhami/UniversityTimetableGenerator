import pandas as pd

from models.course import Course


from mapper.base_mapper import BaseMapper

class CourseMapper(BaseMapper):

    def __init__(self, dataframe):
        self.df = dataframe

    def map_courses(self):

        courses = []

        for _, row in self.df.iterrows():

            # Skip blank rows
            if pd.isna(row.get("Course Code")):
                continue

            # Skip supervisor rows
            if str(row.get("Course Code")).upper() == "SUPERVISOR":
                continue

            course = Course(

    school=self.get_str(row, "School"),

    program=self.get_str(row, "Program"),

    year=self.get_str(row, "Year"),

    term=self.get_str(row, "Term"),

    course_code=self.get_str(row, "Course Code"),

    course_title=self.get_str(row, "Course Title"),

    lecture_hours=self.get_int(row, "L"),

    tutorial_hours=self.get_int(row, "T"),

    practical_hours=self.get_int(row, "P"),

    student_count=self.get_int(row, "No of Students"),

    section=self.get_str(row, "Section"),

    final_section=self.get_str(row, "FINAL SECTION"),

    course_type=self.get_str(row, "Course Type"),

    faculty_domain=self.get_str(row, "Faculty Domain"),

    faculty_type=self.get_str(row, "Faculty Type"),

    uid=self.get_str(row, "UID"),

    shift=self.get_str(row, "Shift Timings"),

    groups=self.get_int(row, "Groups", 1)
)

            courses.append(course)

        return courses