from models.scheduled_class import ScheduledClass


class GreedyScheduler:

    def __init__(self, context):

        self.context = context

        self.faculty_schedule = {}

        self.section_schedule = {}

        self.room_schedule = {}

    def generate(self):

        scheduled = []

        for course in self.context.courses:

            allocated = False

            for slot in self.context.timeslots:

                key_faculty = (
                    course.uid,
                    slot.day,
                    slot.shift,
                    slot.period,
                )

                key_section = (
                    course.section,
                    slot.day,
                    slot.shift,
                    slot.period,
                )

                if key_faculty in self.faculty_schedule:
                    continue

                if key_section in self.section_schedule:
                    continue

                room = self.find_room(course)

                if room is None:
                    continue

                key_room = (
                    room.room_number,
                    slot.day,
                    slot.shift,
                    slot.period,
                )

                if key_room in self.room_schedule:
                    continue

                scheduled_class = ScheduledClass(
                    course_code=course.course_code,
                    course_title=course.course_title,
                    section=course.section,
                    faculty_uid=course.uid,
                    room=room.room_number,
                    day=slot.day,
                    shift=slot.shift,
                    period=slot.period,
                    start_time=slot.start_time,
                    end_time=slot.end_time,
                )

                scheduled.append(scheduled_class)

                self.faculty_schedule[key_faculty] = True
                self.section_schedule[key_section] = True
                self.room_schedule[key_room] = True

                allocated = True

                break

            if not allocated:

                print("Unable to schedule:", course.course_code)

        self.context.scheduled_classes = scheduled

        print(f"\nScheduled Classes : {len(scheduled)}")

    def find_room(self, course):

        for room in self.context.rooms:

            if room.capacity >= course.student_count:

                return room

        return None