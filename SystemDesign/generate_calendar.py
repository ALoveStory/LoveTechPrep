from datetime import datetime, timedelta
from icalendar import Calendar, Event
import pytz
from sessions import weeks  # import the 8-week plan

# Timezone
tz = pytz.timezone("America/Chicago")

# Start date: Sunday, Sept 21, 2025 at 3:00 PM CST
base_date = datetime(2025, 10, 13, 15, 0, tzinfo=tz)

# Create calendar
cal = Calendar()
cal.add("prodid", "-//System Design 8 Weeks Multi-Slot//mxm.dk//")
cal.add("version", "2.0")

day_counter = 0  # track offset from base_date

for week_index, week in enumerate(weeks, start=1):
    for session in week:
        # Each session represents a day
        current_start = base_date + timedelta(days=day_counter)

        for title, duration in session["slots"]:
            event = Event()
            event.add("summary", f"{session['day']} – {title}")
            event.add("dtstart", current_start)
            current_end = current_start + timedelta(minutes=duration)
            event.add("dtend", current_end)
            event.add("dtstamp", datetime.now(tz))
            cal.add_component(event)

            # Advance start time for the next slot
            current_start = current_end

        # Move to the next day
        day_counter += 1

# Save file
with open("../Calendars/system_design_8weeks_multislot.ics", "wb") as f:
    f.write(cal.to_ical())

print("✅ ICS file 'system_design_8weeks_multislot.ics' created with all 8 weeks.")
