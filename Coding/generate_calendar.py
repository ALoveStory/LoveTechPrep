# -*- coding: utf-8 -*-
"""
generate_calendar.py
--------------------
Generic script to convert coding interview prep sessions into an .ics calendar.

Usage:
1. Define your daily sessions in sessions.py (indexed by day number).
2. Set the START_DATE here.
3. Run: python generate_calendar.py
4. Produces 'interview_prep.ics' with all events.
"""

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import uuid
import sessions  # your session definitions

OUTPUT_FILE = "interview_prep.ics"
TIMEZONE = ZoneInfo("America/Chicago")

# 🔧 Change this to move the entire schedule
START_DATE = datetime(2025, 9, 21, 18, 0, tzinfo=TIMEZONE)  # Mon 6:00 PM CST


def format_datetime(dt):
    return dt.astimezone(ZoneInfo("UTC")).strftime("%Y%m%dT%H%M%SZ")


def create_event(start, duration_min, title, description):
    uid = str(uuid.uuid4())
    dt_end = start + timedelta(minutes=duration_min)

    return f"""BEGIN:VEVENT
UID:{uid}
DTSTAMP:{format_datetime(datetime.now(TIMEZONE))}
DTSTART:{format_datetime(start)}
DTEND:{format_datetime(dt_end)}
SUMMARY:{title}
DESCRIPTION:{description}
END:VEVENT
"""


def main():
    events = []
    for day_index, day in enumerate(sessions.SESSIONS, start=0):
        # Calculate this day's "base date"
        base_date = START_DATE + timedelta(days=day_index)

        for block in day["blocks"]:
            # Each block has an offset in minutes from the start of the day
            start_time = base_date.replace(
                hour=block["start_hour"],
                minute=block["start_minute"]
            )
            events.append(create_event(
                start_time,
                block["duration_min"],
                block["title"],
                block["description"]
            ))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("BEGIN:VCALENDAR\n")
        f.write("VERSION:2.0\n")
        f.write("PRODID:-//./Calendars/InterviewPrep//EN\n")
        for e in events:
            f.write(e)
        f.write("END:VCALENDAR\n")

    print(f"✅ Generated {OUTPUT_FILE} with {len(events)} events.")


if __name__ == "__main__":
    main()
