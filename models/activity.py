from dataclasses import dataclass


@dataclass
class Activity:

    activity_id: str

    course_code: str

    course_title: str

    section: str

    faculty_uid: str

    activity_type: str        # Lecture / Tutorial / Practical

    duration: int             # periods

    group_no: int

    total_groups: int

    students: int

    room_type: str

    shift: str