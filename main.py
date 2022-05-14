from custom_calendar import Calendar
from data.utils import EventGenerator
from event import Event

data = EventGenerator()
data.generate_data(500)
# data.save('./data.json')
events_data = data.load('./data.json')
# print(events_data, len(events_data))

events = [Event(**event) for event in events_data]

c = Calendar(events)

result = c.get_events_by_date('01-01-2023 00:00')
print(result, len(result))

# c.remove_event('17-05-2022 9:00')
# print(c)
