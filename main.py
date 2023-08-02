# pip3 install neo4j-driver
# python3 example.py
import os
from neo4j import GraphDatabase
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
    def __init__(self, oId, sId, cId, Odate, Ddate, Amount):
        self.oId = oId
        self.sId = sId
        self.cId = cId
        self.Odate = Odate
        self.Ddate = Ddate
        self.Amount = Amount

class ORDER_ITEM:
    def __init__(self, sId, oId, iId, Icount):
        self.sId = sId
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
        readORDER_ITEM = ORDER_ITEM(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3])
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

def create_contract(greeter):
    counter = 0
    for contract in CONTRACT_list:
        if(counter != 0):
            #print(item.vId, item.ctId, item.Sdate, item.Ctime, item.Cname)
            query = ("CREATE (n:Contract {vId: " + contract.vId + ", ctID: " + contract.ctId + ", Sdate: '" + contract.Sdate +
                     "', Ctime: '" + contract.Ctime + "', Cname: '" + contract.Cname + "'})")
            greeter.driver.execute_query(query)
        else:
            counter = counter + 1
    print("Contracts done!")
def create_customer(greeter):
    counter = 0
    for customer in CUSTOMER_list:
        if(counter != 0):
            query = ("CREATE (n:Customer {cId: " + customer.cId + ", Cname: '" + customer.Cname + "', Street: '"
                     + customer.Street + "', City: '" + customer.City + "', StateAb: '" + customer.StateAb +
                     "', Zipcode: '" + customer.Zipcode + "'})")
            greeter.driver.execute_query(query)
        else:
            counter = counter + 1
    print("Customer done!")

def create_employee(greeter):
    counter = 0
    for employee in EMPLOYEE_list:
        if(counter != 0):
            query = ("CREATE (n:Employee {sId: " + employee.sId + ", SSN: " + employee.SSN + ", Ename: '"
                     + employee.Ename + "', Street: '" + employee.Street + "', City: '" + employee.City +
                     "', StateAb: '" + employee.StateAb + "', Zipcode: '" + employee.Zipcode + "', Etype: '" +
                     employee.Etype + "', Bdate: '" + employee.Bdate + "', Sdate: '" + employee.Sdate + "', Edate: '"
                     + employee.Edate + "', Level: '" + employee.Level + "', Asalary: '" + employee.Asalary +
                     "', Agency: '" + employee.Agency + "', Hsalary: '" + employee.Hsalary + "', Institute: '"
                     + employee.Institute + "', Itype: '" + employee.Itype + "'})")
            greeter.driver.execute_query(query)
        else:
            counter = counter + 1
    print("Employee done!")

def create_item(greeter):
    counter = 0
    for item in ITEM_list:
        if(counter != 0):
            query = ("CREATE (n:Item {iId: " + item.iId + ", Iname: '" +
                     item.Iname + "', Sprice: " + item.Sprice + "})")
            greeter.driver.execute_query(query)
        else:
            counter = counter + 1
    print("Item done!")

def create_oldprice(greeter):
    counter = 0
    #unique_query = ("DROP CONSTRAINT imp_uniq_Old Price_iId]")
    #greeter.driver.execute_query(unique_query)
    for oldprice in OLDPRICE_list:
        if(counter != 0):
            query = ("CREATE (n:`Old Price` {iId: " + oldprice.iId + ", Sprice: " +
                     oldprice.Sprice + ", Sdate: '" + oldprice.Sdate + "', Edate: '" + oldprice.Edate + "'})")
            greeter.driver.execute_query(query)
        counter = counter + 1
    print("Old Price done!")

def create_order_item(greeter):
    counter = 0
    for order_item in ORDER_ITEM_list:
        if(counter != 0):
            query = ("MERGE (n:`Order Item` {sId: " + order_item.sId + ", oId: " + order_item.oId + ", iId: " +
                     order_item.iId + ", Sdate: " + order_item.Icount + "})")
            greeter.driver.execute_query(query)
        counter = counter + 1
    print("Order Item done!")

def create_order(greeter):
    counter = 0
    for orders in ORDERS_list:
        if(counter != 0):
            query = ("CREATE (n: Orders {oId: " + orders.oId + ", sId: " +
                     orders.sId + ", cId: " + orders.cId + ", Odate: '" + orders.Odate + "', Ddate: '" +
                     orders.Ddate + "', Amount: " + orders.Amount + "})")
            greeter.driver.execute_query(query)
        else:
            counter = counter + 1
    print("Orders done!")

def create_store(greeter):
    counter = 0
    for store in STORE_list:
        if(counter != 0):
            query = ("CREATE (n: Store {sId: " + store.sId + ", Sname: '" +
                     store.Sname + "', Street: '" + store.Street + "', City: '" + store.City + "', StateAb: '" +
                     store.StateAb + "', ZipCode: '" + store.Zipcode + "', Sdate: '" + store.Sdate + "', Telno: '" +
                     store.Telno + "', URL: '" + store.URL + "'})")
            greeter.driver.execute_query(query)
        else:
            counter = counter + 1
    print("Store done!")

def create_vendor(greeter):
    counter = 0
    for vendor in VENDOR_list:
        if(counter != 0):
            query = ("CREATE (n: Vendor {vId: " + vendor.vId + ", Vname: '" +
                     vendor.Vname + "', Street: '" + vendor.Street + "', City: '" + vendor.City
                      + "', StateAb: '" + vendor.StateAb + "', ZipCode: '" + vendor.Zipcode + "'})")
            greeter.driver.execute_query(query)
        else:
            counter = counter + 1
    print("Vendor done!")

def create_vendor_item(greeter):
    counter = 0
    for vendor_item in VENDOR_ITEM_list:
        if(counter != 0):
            query = ("CREATE (n:`Vendor Item` {vId: " + vendor_item.vId + ", iId: " +
                     vendor_item.iId + ", Vprice: " + vendor_item.Vprice + "})")
            greeter.driver.execute_query(query)
        counter = counter + 1
    print("Vendor Item done!")
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


class DBDriver:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("MATCH (n:Contract) "
                        "RETURN n", message=message)
        return result.single()[0]


def main():
    greeter = DBDriver("bolt://44.201.15.215:7687", "neo4j", "envelope-partition-cents")
    greeter.driver.execute_query("MATCH (n) DELETE n")
    #greeter.driver.execute_query("CREATE (n:`Order Item` {oId: 1, iId: 2, Icount: 3})")
    #test = greeter.driver.execute_query("MATCH (n:`Order Item`) RETURN n")
    #print(test)

    fname = input("Press Enter to read Data")

    from neo4j import GraphDatabase

    # URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
    URI = "bolt://44.201.15.215:7687"
    AUTH = ("neo4j", "envelope-partition-cents")

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()

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
    print("Data extraction complete.")
    fname = input("Press Enter to export Data")

    create_contract(greeter)
    create_customer(greeter)
    create_employee(greeter)
    create_item(greeter)
    create_oldprice(greeter)
    create_order_item(greeter)
    create_order(greeter)
    create_store(greeter)
    create_vendor(greeter)
    create_vendor_item(greeter)

    greeter.close()
main()