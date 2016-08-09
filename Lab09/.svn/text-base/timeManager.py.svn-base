import timeDuration
def getTotalEventSpan(eventName):
    with open("Events.txt","r") as file:
        lines=file.readlines()
        weeks=0
        days=0
        hours=0
        for line in lines[2:]:
            if eventName == line.split()[0]:
                iteration=line.split()[2]
                if line.split()[1][2] == 'w':
                    weeks+=int(iteration)*int(line.split()[1][:-1])
                if line.split()[1][2] == 'd':
                    days+=int(iteration)*int(line.split()[1][:-1])
                if line.split()[1][2] == 'h':
                    hours+=int(iteration)*int(line.split()[1][:-1])
    return timeDuration.TimeSpan(weeks,days,hours)

def rankEventsBySpan(*args):
    l=[]
    for item in args:
        time=getTotalEventSpan(item)
        for event in l:
            if time > getTotalEventSpan(event):
                l.insert(event.index(),event)
    return l