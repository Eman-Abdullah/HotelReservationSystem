from datetime import date
from src.reservation import Reservation
from src.reservation import Reservation
from datetime import date
from dateutil.relativedelta import relativedelta


dateToday = date.today()


def main():
    dRooms = int(input("How many deluxe rooms are in the hotel : "))
    eRooms = int(input("How many Executive rooms are in the hotel : "))
    sRooms = int(input("How many Suite rooms are in the hotel : "))
    availableDays = int(input("For how many days the hotel will be opened : "))
    reservation = Reservation(sRooms, dRooms, eRooms, availableDays)
    try:
        services = int(input("What do you wanna do choose one the following number \n1: Add Customer\n2: Make Reservation\n3: Modify Reservation\n4: Cancel Reservation\n5: Get Reservation Details\n6: To Exit.\nEnter one of the following number:-"))
    except ValueError:
        print("Please Enter number from the menu")
        services = int(input("What do you wanna do choose one the following number \n1: Add Customer\n2: Make Reservation\n3: Modify Reservation\n4: Cancel Reservation\n5: Get Reservation Details\n6: To Exit.\nEnter one of the following number:-"))
    while(services != 6):
        if (services == 1):
            fname = input("Enter First Name : ")
            lname = input("Enter last name : ")
            no_of_guest = int(input("Enter number of guests : "))
            phone_number = int(input("Enter Phone Number of Customer : "))
            reservation.addCustomer(fname=fname, lname=lname, numGuests=no_of_guest, number=phone_number)
        elif (services == 2):
            customerId = input("Enter customer id : ")
            checkin = input("Enter Check In Date : ")
            year,month,day = checkin.split('-')
            checkinDate = date(int(year), int(month), int(day))
            checkout = input("Enter Check Out Date : ")
            year,month,day = checkout.split('-')
            checkoutDate = date(int(year), int(month), int(day))
            reservation.makeReservation(ID=customerId, chkInDate=checkinDate, chkOutDate=checkoutDate)
        elif (services == 3):
            customerId = input("Enter customer id : ")
            checkin = input("Enter Check In Date : ")
            year,month,day = checkin.split('-')
            checkinDate = date(int(year), int(month), int(day))
            checkout = input("Enter Check Out Date : ")
            year,month,day = checkout.split('-')
            checkoutDate = date(int(year), int(month), int(day))
            reservation.modifyReservation(ID=customerId, newInDate=checkinDate, newOutDate= checkoutDate)
        elif (services == 4):
            customerId = input("Enter customer id : ")
            reservation.cancelReservation(ID=customerId)
        elif (services == 5):
            customerId = input("Enter customer id : ")
            reservation.returnReservationDetails(ID=customerId)
        elif (services == 6):
            print("Thank you for using Hotel Reservation System")
            break
        else:
            print("Please Enter correct input")
        try:
            services = int(input("What do you wanna do choose one the following number \n1: Add Customer\n2: Make Reservation\n3: Modify Reservation\n4: Cancel Reservation\n5: Get Reservation Details\n6: To Exit.\nEnter one of the following number:-"))
        except ValueError:
            print("Please Enter number from the menu")
            services = int(input("What do you wanna do choose one the following number \n1: Add Customer\n2: Make Reservation\n3: Modify Reservation\n4: Cancel Reservation\n5: Get Reservation Details\n6: To Exit.\nEnter one of the following number:-"))
        
main()

def test_Case3(capsys):
    
    

    dateVin = dateToday + relativedelta(days = 1)
    dateVout = dateToday + relativedelta(days = 7)
    dateVout2 = dateToday + relativedelta(days = 11)
    dateJin = dateToday + relativedelta(days = 5)
    dateJout = dateToday + relativedelta(days = 13)
    
    reservation = Reservation(1, 1, 1, 30)
    reservation.addCustomer('Emaan', 'Abdullah', 0, 123456789)
    reservation.addCustomer('John', 'Doe', 0, 123456789)
    reservation.makeReservation('EA6789', dateVin, dateVout, "1S")
    reservation.makeReservation('EA6789', dateVin, dateVout2)
    reservation.makeReservation('JD6789', dateJin, dateJout, "1E")
    output = []
    with open("testCase3.txt", 'r') as f:
        for i in f.readlines():
            output.append(i)
    captured = capsys.readouterr()
    for i in output:
        assert i in captured.out
    

def test_Case4(capsys):
    
   
    
    dateVIn = dateToday
    dateOut = dateToday + relativedelta(days = 3)
    dateOut2 = dateToday + relativedelta(days = 6)
    dateOut3 = dateToday + relativedelta(days = 4)
    
    reservation = Reservation(0, 1, 0, 6)
    reservation.addCustomer('Emaan', 'Abdullah', 0, 123456789)
    reservation.addCustomer('John', 'Doe', 0, 123456789)
    reservation.makeReservation('EA6789', dateVIn, dateOut, '1D')
    reservation.makeReservation('JD6789', dateOut, dateOut2, '1D')
    reservation.modifyReservation('EA6789', dateVIn, dateOut3, '1D')
    output = []
    with open("testCase4.txt", 'r') as f:
        for i in f.readlines():
            output.append(i)
    captured = capsys.readouterr()
    for i in output:
        assert i in captured.out
def test_Case5(capsys):
    
    
    date1 = dateToday
    date2 = dateToday + relativedelta(days = 3)
    date3 = dateToday + relativedelta(days = 6)
    date4 = dateToday + relativedelta(days = 9)
    
    reservation = Reservation(10, 10, 10, 45)
    reservation.addCustomer('Emaan', 'Abdullah', 0, 123456789)
    reservation.addCustomer('David', 'Venuto', 0, 123456789)
    reservation.makeReservation('EA6789', date1, date2, '1D')
    reservation.makeReservation('DV6789', date3, date4, '2D')
    
    reservation.modifyReservation('EA6789', date1, date4, '10E')
    output = []
    with open("testCase5.txt", 'r') as f:
        for i in f.readlines():
            output.append(i)
    captured = capsys.readouterr()
    for i in output:
        assert i in captured.out
    
    
    