def event_summary (event_name,total, status):
    return f"{event_name}: total{total} naira, {status}."

#required example
event_name = "study_day"
print(event_summary(event_name, 'total', 'status'))

#one different event name and total
event_name = "Chioma day"
print (event_summary(event_name, 'total', 'status2'))
