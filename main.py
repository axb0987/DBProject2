# pip3 install neo4j-driver
# python3 example.py
import os

class CUSTOMER:
    def __init__(self, cId, Cname, Street, City, StateAb, Zipcode):
        self.cId = cId
        self.Cname = Cname
        self.Street = Street
        self.City = City
        self.StateAb = StateAb
        self.Zipcode = Zipcode

class ITEM:
    def __init__(self, iId, Iname, Sprice):
        self.iId = iId
        self.Iname = Iname
        self.Sprice = Sprice

class VENDOR:
    def __init__(self, vId, Vname, Street, City, StateAb, Zipcode):
        self.vId = vId
        self.Vname = Vname
        self.Street = Street
        self.City = City
        self.StateAb = StateAb
        self.Zipcode = Zipcode

class VENDOR_ITEM:
    def __init__(self, vId, iId, Vprice):
        self.vId = vId
        self.iId = iId
        self.Vprice = Vprice

class STORE:
    def __init__(self, sId, Sname, Street, City, StateAb, Zipcode, Sdate, Telno, URL):
        self.sId = sId
        self.Sname = Sname
        self.Street = Street
        self.City = City
        self.StateAb = StateAb
        self.Zipcode = Zipcode
        self.Sdate = Sdate
        self.Telno = Telno
        self.URL = URL

class ORDERS:
    def __init__(self, oId, sId, Odate, Ddate, Amount, cId):
        self.oId = oId
        self.sId = sId
        self.Odate = Odate
        self.Ddate = Ddate
        self.Amount = Amount
        self.cId = cId

#class ORDER_ITEM:
    #def __init__(self, oId, sId, iId, Icount):
        #self.oId = oId
        #self.sId = sId
        #self.iId = iId
        #self.Icount = Icount

class ORDER_ITEM:
    def __init__(self, oId, iId, Icount):
        self.oId = oId
        self.iId = iId
        self.Icount = Icount

class EMPLOYEE:
    def __init__(self, sId, SSN, Ename, Etype, Bdate, Sdate, Edate, Level, Asalary, Agency, Hsalary, Institute, Itype, Street, City, StateAb, Zipcode):
        self.sId = sId
        self.SSN = SSN
        self.Ename = Ename
        self.Etype = Etype
        self.Bdate = Bdate
        self.Sdate = Sdate
        self.Edate = Edate
        self.Level = Level
        self.Asalary = Asalary
        self.Agency = Agency
        self.Hsalary = Hsalary
        self.Institute = Institute
        self.Itype = Itype
        self.Street = Street
        self.City = City
        self.StateAb = StateAb
        self.Zipcode = Zipcode

class CONTRACT:
    def __init__(self, vId, ctId, Sdate, Ctime, Cname):
        self.vId = vId
        self.ctId = ctId
        self.Sdate = Sdate
        self.Ctime = Ctime
        self.Cname = Cname

class OLDPRICE:
    def __init__(self, iId, Sprice, Sdate, Edate):
        self.iId = iId
        self.Sprice = Sprice
        self.Sdate = Sdate
        self.Edate = Edate

CONTRACT_list = []
CUSTOMER_list = []
EMPLOYEE_list = []
ITEM_list = []
OLDPRICE_list = []
ORDER_ITEM_list = []
ORDERS_list = []
STORE_list = []
VENDOR_list = []
VENDOR_ITEM_list = []

def read_CONTRACT(data):
    for line in data:
        line = line.rstrip()
        lineSplit = line.split(",")
        readCONTRACT = CONTRACT(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4])
        CONTRACT_list.append(readCONTRACT)
    #tester print statement
    #for item in CONTRACT_list:
        #print(item.vId, item.ctId, item.Sdate, item.Ctime, item.Cname)

def read_CUSTOMER(data):
    for line in data:
        line = line.rstrip()
        lineSplit = line.split(",")
        readCUSTOMER = CUSTOMER(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4], lineSplit[5])
        CUSTOMER_list.append(readCUSTOMER)

def read_EMPLOYEE(data):
    for line in data:
        line = line.rstrip()
        lineSplit = line.split(",")
        readEMPLOYEE = EMPLOYEE(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4], lineSplit[5], lineSplit[6], lineSplit[7], lineSplit[8], lineSplit[9], lineSplit[10], lineSplit[11], lineSplit[12], lineSplit[13], lineSplit[14], lineSplit[15], lineSplit[16])
        EMPLOYEE_list.append(readEMPLOYEE)

def read_ITEM(data):
    for line in data:
        line = line.rstrip()
        lineSplit = line.split(",")
        readITEM = ITEM(lineSplit[0], lineSplit[1], lineSplit[2])
        ITEM_list.append(readITEM)

def read_OLDPRICE(data):
    for line in data:
        line = line.rstrip()
        lineSplit = line.split(",")
        readOLDPRICE = OLDPRICE(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3])
        OLDPRICE_list.append(readOLDPRICE)

def read_ORDER_ITEM(data):
    for line in data:
        line = line.rstrip()
        lineSplit = line.split(",")
        readORDER_ITEM = ORDER_ITEM(lineSplit[0], lineSplit[1], lineSplit[2])
        ORDER_ITEM_list.append(readORDER_ITEM)

def read_ORDERS(data):
    for line in data:
        line = line.rstrip()
        lineSplit = line.split(",")
        readORDERS = ORDERS(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4], lineSplit[5])
        ORDERS_list.append(readORDERS)

def read_STORE(data):
    for line in data:
        line = line.rstrip()
        lineSplit = line.split(",")
        readSTORE = STORE(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4], lineSplit[5], lineSplit[6], lineSplit[7], lineSplit[8])
        STORE_list.append(readSTORE)

def read_VENDOR(data):
    for line in data:
        line = line.rstrip()
        lineSplit = line.split(",")
        readVENDOR = VENDOR(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4], lineSplit[5])
        VENDOR_list.append(readVENDOR)

def read_VENDOR_ITEM(data):
    for line in data:
        line = line.rstrip()
        lineSplit = line.split(",")
        readVENDOR_ITEM = VENDOR_ITEM(lineSplit[0], lineSplit[1], lineSplit[2])
        VENDOR_ITEM_list.append(readVENDOR_ITEM)

def read_operations(fname):
    cwd = os.getcwd()
    os.chdir(cwd)
    file = (fname + ".csv")
    try:
        f = open(file, 'r')
    except IOError:
        print("File not found.")
        exit()

    data = f.readlines()

    #The only reason I am using a switch statement is because older versions of python do not support it.
    if(fname == "CONTRACT"):
        read_CONTRACT(data)
    elif(fname == "CUSTOMER"):
        read_CUSTOMER(data)
    elif (fname == "EMPLOYEE"):
        read_EMPLOYEE(data)
    elif (fname == "ITEM"):
        read_ITEM(data)
    elif (fname == "OLDPRICE"):
        read_OLDPRICE(data)
    elif (fname == "ORDER_ITEM"):
        read_ORDER_ITEM(data)
    elif (fname == "ORDERS"):
        read_ORDERS(data)
    elif (fname == "STORE"):
        read_STORE(data)
    elif (fname == "VENDOR"):
        read_VENDOR(data)
    elif (fname == "VENDOR_ITEM"):
        read_VENDOR_ITEM(data)

    f.close()

def main():
    fname = input("Type name of file without .csv: ")
    read_operations("CONTRACT")
    read_operations("CUSTOMER")
    read_operations("EMPLOYEE")
    read_operations("ITEM")
    read_operations("OLDPRICE")
    read_operations("ORDER_ITEM")
    read_operations("ORDERS")
    read_operations("STORE")
    read_operations("VENDOR")
    read_operations("VENDOR_ITEM")

main()