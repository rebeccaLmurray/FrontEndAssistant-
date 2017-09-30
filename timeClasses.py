class Time():
    def __init__ (self, timeString):
        global hour, minute
        self.timeString = timeString
        hour,minute = (timeString.split(":"))
        hour = int( hour )
        minute = int( minute )

    def getTime( self ):
        return self.timeString

    def getHour(self):
        return hour

    def getMinute(self):
        return minute
