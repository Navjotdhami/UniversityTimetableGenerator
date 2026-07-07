from datetime import datetime, timedelta

from scheduler.time_slot import TimeSlot


class TimeSlotGenerator:

    DAYS = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
    ]

    SHIFT_STARTS = {
        1: "08:00",
        2: "09:00",
        3: "10:00",
    }

    PERIODS = 8

    PERIOD_DURATION = 50

    def generate(self):

        slots = []

        for day in self.DAYS:

            for shift, start in self.SHIFT_STARTS.items():

                current = datetime.strptime(start, "%H:%M")

                for period in range(1, self.PERIODS + 1):

                    end = current + timedelta(minutes=self.PERIOD_DURATION)

                    slots.append(
                        TimeSlot(
                            day=day,
                            shift=shift,
                            period=period,
                            start_time=current.strftime("%H:%M"),
                            end_time=end.strftime("%H:%M"),
                        )
                    )

                    current = end

        return slots