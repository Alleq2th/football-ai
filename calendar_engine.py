"""
Calendar Engine V1

Responsible for:

- Daily content schedules
- Content slot creation
- Trend assignment
- Future event assignment
"""

from datetime import datetime


class CalendarSlot:

    def __init__(

        self,
        time,
        content_type,
        trend=None

    ):

        self.time = time

        self.content_type = content_type

        self.trend = trend

        self.status = "Pending"

    def to_dict(self):

        return {

            "time": self.time,

            "content_type": self.content_type,

            "trend": self.trend,

            "status": self.status

        }


class CalendarEngine:

    def __init__(self):

        self.slots = []

    def create_schedule(

        self,
        posting_times

    ):

        self.slots = []

        for time in posting_times:

            slot = CalendarSlot(

                time=time,

                content_type="Auto"

            )

            self.slots.append(slot)

        return self.slots

    def assign_trend(

        self,
        slot_index,
        trend_title

    ):

        if slot_index < len(self.slots):

            self.slots[slot_index].trend = trend_title

            return True

        return False

    def mark_complete(

        self,
        slot_index

    ):

        if slot_index < len(self.slots):

            self.slots[slot_index].status = "Completed"

            return True

        return False

    def get_schedule(self):

        return [

            slot.to_dict()

            for slot in self.slots

        ]


if __name__ == "__main__":

    calendar = CalendarEngine()

    calendar.create_schedule([

        "8:00 AM",

        "12:00 PM",

        "6:00 PM"

    ])

    calendar.assign_trend(

        0,

        "World Cup Final"

    )

    print(

        calendar.get_schedule()

  )
