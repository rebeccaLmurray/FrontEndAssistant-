import timeClasses

class Associate():
    def __init__(self, name, station, startTime, endTime):
        self.name = name
        self.station = station
        self.startTime = timeClasses.Time( startTime )
        self.endTime = timeClasses.Time( endTime )

    def getName( self ):
        return self.name

    def getStation( self ):
        return self.station
    
    def getStartTime( self ):
        return self.startTime.getTime()

    def getEndTime( self ):
        return self.endTime.getTime()
    
    def getSchedule( self ):
        return "| " + self.name + " | " + self.startTime.getTime() + " | " + self.endTime.getTime()
    
