from dataclasses import dataclass, field


@dataclass
class Faculty:

    faculty_id: str

    weekly_load: int = 0

    max_load: int = 23

    assigned_courses: list = field(default_factory=list)

    assigned_slots: list = field(default_factory=list)

    is_dummy: bool = False