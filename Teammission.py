#PHASE 1
# Joy David - participant_cost
# Kelechi   - event_total
# Anderson  - budget_status
# Chioma    - budget_summary



def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees * (food_per_person + transport_per_person)

#Normal attendee count 
print (participant_cost (10, 800, 200))
#Zero attendee count
print (participant_cost (0, 800, 200))


#"""
#Joy handover note
#component: participant_cost
#return : attendees * (food_per_person + transport_per_person)
#tests: normal, zero
#issue : none

#"""

def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    cost = participant_cost(attendees, food_per_person, transport_per_person)
    return cost + venue_cost
#Normal attendee cost 
total = event_total (10, 800, 200, 5000)
print (total)
#Zero attendees 
total1 = event_total(0, 800, 200, 5000)
print (total1)

#"""
 #Kelechi handover note
#component: event_total
#return : cost + venue
#tests: normal, zero
#issue : none
   
#"""
budget = 16000

def budget_status(budget, total):
    if total <= budget:
        return "Within budget"
    else:
        return "Over budget"
 
# below budget when budget = 16000
status = budget_status(budget, total)
print(status)    

# over budget when budget = 16000
status2 = budget_status(total, budget)
print(status2)

#"""

#Anderson handover note
#component: budget_status
#return : within budget, over budget
#tests: below, over
#issue : none
#"""

def event_summary (event_name, total, status):
    return f"{event_name}: total {total} naira. {status}."
 
 #required example
event_name = "study_day"
print(event_summary(event_name, total, status))

# One different event name and total
event_name = "Chioma_day"
print(event_summary(event_name, total, status2))

#"""
#Chioma handover note
#component: budget_summary
#return : return f"{event_name}: total {total} naira. {status}."
#tests: required example, one different name
#issue : none
#"""


