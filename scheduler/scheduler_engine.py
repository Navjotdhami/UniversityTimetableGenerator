from scheduler.time_slot_generator import TimeSlotGenerator


class SchedulerEngine:

    def __init__(self, context):

        self.context = context

        self.timeslot_generator = TimeSlotGenerator()

    def initialize(self):

        self.context.timeslots = self.timeslot_generator.generate()

        print("\nScheduler Initialized")

        print(f"Available Time Slots : {len(self.context.timeslots)}")