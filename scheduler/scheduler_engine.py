from scheduler.time_slot_generator import TimeSlotGenerator
from scheduler.constraint_scheduler import ConstraintScheduler


class SchedulerEngine:

    def __init__(self, context):

        self.context = context

        self.timeslot_generator = TimeSlotGenerator()
        self.constraint_scheduler = ConstraintScheduler(context)

    def initialize(self):

        self.context.timeslots = self.timeslot_generator.generate()

        print("\nScheduler Initialized")
        print(f"Available Time Slots : {len(self.context.timeslots)}")

    def generate_timetable(self):

        print("\nStarting timetable generation...")

        if not self.context.activities:
            raise Exception("No activities found in SchedulerContext.")

        self.context.assignments = self.constraint_scheduler.schedule(
            self.context.activities,
            self.context.timeslots
        )

        print(f"\nScheduled Classes : {len(self.context.assignments)}")

        return self.context.assignments