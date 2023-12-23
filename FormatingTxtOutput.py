import icsGenerate
from icalendar import Calendar, Event
from datetime import datetime, timedelta

startday = datetime(2023, 12, 11, 0, 0, 0)
slotName = {"Slot1" : 7, "Slot2": 9.5, "Slot3": 13, "Slot4": 15.5, "Slot5": 18, "Slot6": 16.25, "Slot7": 16, "Slot8": 17}
subjName = [ "DSA103"]


with open("output3.txt", "r") as file:
    text = file.readlines()
    
    
    for line in text:
        skipCount = 0 # used to map the day to the event
        line = line.replace(" ","") # used to cut off space in lines
        if line[0:5] in slotName: # Slotx takes 5 spaces
            time = slotName[line[0:5]] # timestamp of the event
            line = line[5::] # cut off the slotx
            print(time)
        for index, char in enumerate(line): # reading each character in a line
            if char == "-": 
                skipCount += 1 # each - is counted as a day skip
                continue
            elif line[index:index + 6] in subjName:
                line.replace(line[index + 6], "") # cut off the + or - after each subject
                
                print("This is the index:", line[index: index + 6])
                eventSummay = line[index: index + 6]
                eventDstart = startday + timedelta(days=skipCount) + timedelta(hours= time)
                eventDend = startday + timedelta(days=skipCount) + timedelta(hours= time + 2.25)
                eventLocation = "sample location"
                eventDescription = "sample description"
                icsGenerate.create_ics_file(eventSummay, eventDescription, eventLocation, eventDstart, eventDend)
