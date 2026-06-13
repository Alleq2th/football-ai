"""
Posting Frequency Database

Controls how often creators post
and suggested posting schedules.
"""

POSTING_FREQUENCIES = {

    1: [
        "12:00 PM"
    ],

    3: [
        "9:00 AM",
        "2:00 PM",
        "7:00 PM"
    ],

    5: [
        "8:00 AM",
        "11:00 AM",
        "2:00 PM",
        "5:00 PM",
        "8:00 PM"
    ],

    7: [
        "7:00 AM",
        "9:00 AM",
        "11:00 AM",
        "1:00 PM",
        "3:00 PM",
        "6:00 PM",
        "9:00 PM"
    ],

    10: [
        "7:00 AM",
        "8:30 AM",
        "10:00 AM",
        "11:30 AM",
        "1:00 PM",
        "2:30 PM",
        "4:00 PM",
        "5:30 PM",
        "7:00 PM",
        "9:00 PM"
    ],

    15: [
        "6:00 AM",
        "7:00 AM",
        "8:00 AM",
        "9:00 AM",
        "10:00 AM",
        "11:00 AM",
        "12:00 PM",
        "1:00 PM",
        "2:00 PM",
        "3:00 PM",
        "4:00 PM",
        "5:00 PM",
        "6:00 PM",
        "8:00 PM",
        "10:00 PM"
    ]
}


def get_available_frequencies():

    return list(POSTING_FREQUENCIES.keys())


def get_schedule(posts_per_day):

    return POSTING_FREQUENCIES.get(posts_per_day, [])


def frequency_exists(posts_per_day):

    return posts_per_day in POSTING_FREQUENCIES


if __name__ == "__main__":

    print("AVAILABLE FREQUENCIES")
    print(get_available_frequencies())

    print("\n5 POSTS PER DAY")
    print(get_schedule(5))
