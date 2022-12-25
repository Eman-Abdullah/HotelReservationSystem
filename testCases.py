from src.reservation import Reservation
from operator import attrgetter
from datetime import date
from dateutil.relativedelta import relativedelta


dateToday = date.today()

def test_Case1(capsys):
    
    
    dateIn = dateToday
    dateOut = dateToday + relativedelta(days = 1)
    reservation = Reservation(0, 0, 0, 0)
    reservation.addCustomer('Emaan', 'Abdullah', 0, 1234567891)
    reservation.makeReservation('EA7891', dateIn, dateOut, '1S')
    reservation.addCustomer('John', 'Doe', 0, 1234567891)
    
    reservation.makeReservation('JD7891', dateIn, dateOut, '1S')
    captured = capsys.readouterr()
    
    assert captured.out.split('\n')[-2] == 'JD7891 :Hotel is sold out for the selected dates!'
    
    
    

def test_Case2(capsys):
    
    
    dateIn = dateToday
    dateOut = dateToday + relativedelta(days = 1)
    
    reservation = Reservation(1, 0, 0, 1)
    reservation.addCustomer('Emaan', 'Abdullah', 0, 1234567891)
    reservation.addCustomer('John', 'Doe', 0, 1234567891)
    reservation.makeReservation('EA7891', dateIn, dateOut, '1S')
    reservation.cancelReservation('EA7891')
    reservation.makeReservation('JD7891', dateIn, dateOut,'1S')
    output = ''
    with open("testCase2.txt", 'r') as f:
        for i in f.readlines():
            output+=i
    reservation.makeReservation('JD7891', dateIn, dateOut, '1S')
    captured = capsys.readouterr()
    assert captured.out == output
    
    
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
    output = ''
    with open("testCase3.txt", 'r') as f:
        for i in f.readlines():
            output+=i
    captured = capsys.readouterr()
    assert captured.out == output
    

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
    output = ''
    with open("testCase4.txt", 'r') as f:
        for i in f.readlines():
            output+=i
    captured = capsys.readouterr()
    assert captured.out == output
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
    output = ''
    with open("testCase5.txt", 'r') as f:
        for i in f.readlines():
            output+=i
    captured = capsys.readouterr()
    assert captured.out == output
    
    
    