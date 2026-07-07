from dataclasses import dataclass

from models.course import Course
from models.faculty import Faculty
from models.room import Room
from models.timeslot import TimeSlot


@dataclass
class Allocation:

    course: Course

    faculty: Faculty

    room: Room

    timeslot: TimeSlot