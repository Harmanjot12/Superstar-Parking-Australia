from datetime import datetime
from datetime import date

class Parking:
    outday = ""
    outtime  = ""
    pay = 0 
    def __init__(self,carnum,inday,intime):
        
        self.carnum = carnum
        self.inday  = inday
        self.intime = intime
        

    #access method (get method)
    def getcarnum(self):
        return self.carnum
   
    def getinday(self):
        return self.inday
    
    def getintime(self):
        return self.intime
   
    def getoutday(self):
        return self.outday
    
    def getouttime(self):
        return self.outtime
    
    def getpay(self):
        return self.pay
    


    #mutator method (set method) 
    def setcarnum(self,carnum):
        self.carnum = carnum
        
    def setinday(self,inday):
        self.inday = inday
    
    def setintime(self,intime):
        self.intime = intime

    def setoutday(self,outday):
        self.outday = outday
    
    def setouttime(self,outtime):
        self.outtime = outtime
        self.calamount()
    
    def calamount(self):
        
        datetimeFormat = '%d/%m/%Y'
        self.staydays = datetime.strptime(self.outday, datetimeFormat) - datetime.strptime(self.inday, datetimeFormat)
        self.days = self.staydays.days
        
        
        datetimeFormat = '%H:%M:%S'
        self.staytime = datetime.strptime(self.outtime, datetimeFormat) - datetime.strptime(self.intime, datetimeFormat)
        self.sec = self.staytime.seconds
        self.minute = self.sec / 60
        self.hour = self.minute / 60 

        
        if self.days>1:
            self.pay = self.stayday * 20    #$20 per day  
        
        elif self.days<=1:
            if self.hour<10:
                self.pay = 5    #$5 for less than 10 hours
            
            elif self.hour>=10 and self.hour>=24:
                self.pay = 10    #$10 for less than 24 hours and greater than 9 hours
        
        else:
            print("Sorry ! Time is invalid")
            
            
        
