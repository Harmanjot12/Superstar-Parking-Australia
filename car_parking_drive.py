from car_parking import Parking
import pickle
from datetime import datetime
from datetime import date
import sys

#creating list of for records
record = []


#select weather car enters or exits
def option():
    while(True):
        print("\t\t\t \t\t **Heartest Welcome to Superstar Parking Australia** \n")
        
        #input number accoding to requirement        
        print("Please choose one of the following option")
        print("1.Car Entry")
        print("2.Car Exit ")
        print("3.View Car Details ")
        print("4.Close the program ")
        
        option = int(input("Your Option --> "))
    
    
        if option==1:
            carentry()
        
        elif option==2:
            carexits()
        
        elif option==3:
            carview()
        
        elif option==4:
            print("We are closed Now")
            sys.exit()

        
        else:
            option()
        


#option 1 when car enters
def carentry():
   
    while(True):
        number = input("Enter Car Number : ")
        num = number.upper()
        now = datetime.now()
        intime = now.strftime("%H:%M:%S")
        today = date.today()
        inday = today.strftime("%d/%m/%Y")
        
        obj = Parking(num,inday,intime)
        record.append(obj)
        
        print("\n\n------------------------------------------------")
        print("Hey ! " + " " + num + " "+ "We Welcome's you")
        print("\nYour car is safe at Superstar Parking Australia ")
        print("------------------------------------------------\n\n")
            
        #asking user weather they want to enter more values or not
        more = input("Want to enter more : ")
        more = more.lower()
        if (more=='n'):
            print("\n\n")
            break
        

    with open("cars-parked-w.bin" , "wb") as f:
        pickle.dump(record,f)
           
    f.close()




#option 2 when car enters
def carexits():
   
    while(True):
        number = input("Enter Car Number : ")
        num = number.upper()
        
        
        for s in record:
            if num==s.getcarnum():
                now = datetime.now()
                time = now.strftime("%H:%M:%S")
                today = date.today()
                day = today.strftime("%d/%m/%Y")
            
                s.setoutday(day)
                s.setouttime(time)
                
                print("\n\n-------------------------------")
                print("Car Number    - " + str(s.getcarnum()))
                print("Enter's On    - " + s.getinday())
                print("Enter's At    - " + s.getintime())
                print("Exit's On     - " + s.getoutday())
                print("Exit's At     - " + s.getouttime())
                print("Payouts       - " + str(s.getpay()))
                print("**Thanks for Visiting**")
                print("-------------------------------\n\n")
                break
 
        with open("cars-parked-w.bin" , "wb") as f:
           pickle.dump(record,f)
           
               
        
        
        #asking user weather they want to enter more values or not
        more = input("Want to enter more : ")
        more = more.lower()
        if (more=='n'):
            print("\n\n\n")
            break
    
    
    
    

#reading record from binary file
def readdata():
    with open("cars-parked-w.bin" , "rb") as f:
        global record
        record = pickle.load(f)
    f.close()


    
#option 3 to view particular car details    
def carview():
   while(True):
        number = input("Enter Car Number : ")
        num = number.upper()
        
        
        for s in record:
            if num==s.getcarnum():
                print("\n\n--------------------------------")
                print("Car Number    - " + str(s.getcarnum()))
                print("Enter's On    - " + s.getinday())
                print("Enter's At    - " + s.getintime())
                print("Exit's On     - " + s.getoutday())
                print("Exit's At     - " + s.getouttime())
                print("Payouts       - " + str(s.getpay()))
                print("--------------------------------\n\n")
                break
        readdata()
        
    
        
        #asking user weather they want to enter more values or not
        more = input("Want to enter more : ")
        more = more.lower()
        if (more=='n'):
            print("\t\t\t\t\t\tWelcome ! ")
            break
    
    

#calling main function
def main():
    readdata()
    option()

if __name__ == "__main__":
    main()