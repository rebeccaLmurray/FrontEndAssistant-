import timeClasses

class Associate():
    def __init__(self, name, startTime, endTime):
        self.name = name
        self.startTime = timeClasses.Time( startTime )
        self.endTime = timeClasses.Time( endTime )

    def getName( self ):
        return self.name
    
    def getSchedule( self ):
        return self.startTime.getTime() + " - " + self.endTime.getTime()
    
