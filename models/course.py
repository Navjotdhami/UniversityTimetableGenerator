from dataclasses import dataclass


@dataclass
class Course:

    school: str
    program: str
    year: str
    term: str

    course_code: str
    course_title: str

    lecture_hours: int
    tutorial_hours: int
    practical_hours: int

    student_count: int

    section: str
    final_section: str

    course_type: str

    faculty_domain: str
    faculty_type: str

    # NEW
    uid: str

    shift: str

    groups: int

    dummy_faculty: str = ""