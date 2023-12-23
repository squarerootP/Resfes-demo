from datetime import datetime, timedelta

startday = datetime(2023, 12, 11, 0, 0, 0)
slotName = {"Slot1" : 7, "Slot2": 9.5, "Slot3": 13, "Slot4": 15.5, "Slot5": 18, "Slot6": 16.25, "Slot7": 16, "Slot8": 17}
subjName = [ "DSA103"]
newText = ""

with open("output2", "r") as file:
    text = file.readlines()
    for line in text:
        line = line.replace(" ","") # used to cut off space in lines
        if line[0:5] in slotName: # Slotx takes 5 spaces
            time = slotName[line[0:5]] # timestamp of the event
            line = line[5::] # cut off the slotx
            newText += f'{line}\n'
print(newText)
skipCount = 4
time = 7
eventDstart = startday + timedelta(days=skipCount) + timedelta(hours= time)
eventDend = startday + timedelta(days=skipCount) + timedelta(hours= time + 2.25)
print(eventDstart, eventDend)