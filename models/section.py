from dataclasses import dataclass

@dataclass
class Section:
    section_id: str
    school: str = ""
    program: str = ""
    year: str = ""
    term: str = ""
    student_count: int = 0