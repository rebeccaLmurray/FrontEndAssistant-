class Associate():
    def __init__(self, name, startTime, endTime):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime

    def getName( self ):
        return self.name
    
    def getSchedule( self ):
        return self.startTime + " - " + self.endTime
    
