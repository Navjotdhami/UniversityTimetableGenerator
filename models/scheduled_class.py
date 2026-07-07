from dataclasses import dataclass


@dataclass
class ScheduledClass:

    course_code: str

    course_title: str

    section: str

    faculty_uid: str

    room: str

    day: str

    shift: int

    period: int

    start_time: str

    end_time: str