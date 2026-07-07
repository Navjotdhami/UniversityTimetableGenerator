from dataclasses import dataclass, field


@dataclass
class UniversityDatabase:

    courses: list = field(default_factory=list)

    sections: list = field(default_factory=list)

    faculties: list = field(default_factory=list)

    rooms: list = field(default_factory=list)

    labs: list = field(default_factory=list)

    constraints: list = field(default_factory=list)