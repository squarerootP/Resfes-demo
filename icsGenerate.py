from icalendar import Calendar, Event
from datetime import datetime, timedelta

def create_ics_file(summary, description, location, start_datetime, end_datetime):
    cal = Calendar()

    event = Event()
    event.add('summary', summary)
    event.add('description', description)
    event.add('location', location)

    # Ensure that start and end dates are of type datetime
    event.add('dtstart', start_datetime)
    event.add('dtend', end_datetime)

    cal.add_component(event)

    # Write the calendar to a file
    with open('output2.ics', 'ab') as f:
        f.write(cal.to_ical())

# Example usage:
event_summary = 'Sample Event'
event_description = 'This is a sample event description.'
event_location = 'Sample Location'
start_datetime = datetime(2023, 12, 22, 13, 0, 0)  # 22nd December 2023, 1:00 PM
end_datetime = start_datetime + timedelta(hours=2.25)  # Event duration: 2 hours 15 mins

create_ics_file(event_summary, event_description, event_location, start_datetime, end_datetime)

