from models.scheduled_activity import ScheduledActivity


class ConstraintScheduler:
    """
    Basic scheduler (Phase 1)

    This version simply assigns each activity to the first
    available room and time slot.

    Constraints will be added in later phases.
    """

    def __init__(self, context):
        self.context = context

    def schedule(self, activities, timeslots):

        assignments = []

        if not self.context.rooms:
            raise Exception("No rooms available for scheduling.")

        room = self.context.rooms[0]

        slot_index = 0

        for activity in activities:

            if slot_index >= len(timeslots):
                raise Exception(
                    "Not enough time slots to schedule all activities."
                )

            assignment = ScheduledActivity(
                activity=activity,
                timeslot=timeslots[slot_index],
                room_id=room.room_id
            )

            assignments.append(assignment)

            slot_index += activity.duration

        return assignments