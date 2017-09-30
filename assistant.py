import associate
import timeClasses

class Assistant():    

    def __init__(self):
        global associates, numOfAssociates
        associates = [None] * 255
        numOfAssociates = 0
    
    def addAssociate(self, name, station, startTime, endTime):
        global associates, numOfAssociates
        associates[numOfAssociates] = associate.Associate(name, station, startTime, endTime)
        numOfAssociates += 1

    def getSchedule(self):
        global associates
        for person in associates:
            if person:
                print( person.getSchedule() )

a = Assistant()
a.addAssociate("Bob", "Pro", "8:00", "17:00")
a.addAssociate("Sarah", "Checkouts", "8:00", "17:00")
a.getSchedule()

