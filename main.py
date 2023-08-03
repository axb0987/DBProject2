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
    def __init__(self, sId, SSN, Ename, Etype, Bdate, Sdate, Edate, Level, Asalary, Agency, Hsalary, Institute, Itype,
                 Street, City, StateAb, Zipcode):
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
    # tester print statement
    # for item in CONTRACT_list:
    # print(item.vId, item.ctId, item.Sdate, item.Ctime, item.Cname)


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
        readEMPLOYEE = EMPLOYEE(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4], lineSplit[5],
                                lineSplit[6], lineSplit[7], lineSplit[8], lineSplit[9], lineSplit[10], lineSplit[11],
                                lineSplit[12], lineSplit[13], lineSplit[14], lineSplit[15], lineSplit[16])
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
        readSTORE = STORE(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4], lineSplit[5],
                          lineSplit[6], lineSplit[7], lineSplit[8])
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


def print_nodes(greeter, tag):
    query = ("MATCH (n:" + tag + ") RETURN n")
    total_ret = greeter.driver.execute_query(query)
    match_ret = total_ret[0]
    for nodes in match_ret:
        print(nodes)


def create_contract(greeter, io):
    counter = 0
    for contract in CONTRACT_list:
        if (counter != 0):
            # print(item.vId, item.ctId, item.Sdate, item.Ctime, item.Cname)
            query = (
                        "CREATE (n:Contract {vId: " + contract.vId + ", ctID: " + contract.ctId + ", Sdate: '" + contract.Sdate +
                        "', Ctime: '" + contract.Ctime + "', Cname: '" + contract.Cname + "'})")
            greeter.driver.execute_query(query)
        else:
            counter = counter + 1
    print("Contracts done!")
    if io == 'T':
        print_nodes(greeter, "Contract")


def create_customer(greeter, io):
    counter = 0
    for customer in CUSTOMER_list:
        if (counter != 0):
            query = ("CREATE (n:Customer {cId: " + customer.cId + ", Cname: '" + customer.Cname + "', Street: '"
                     + customer.Street + "', City: '" + customer.City + "', StateAb: '" + customer.StateAb +
                     "', Zipcode: '" + customer.Zipcode + "'})")
            greeter.driver.execute_query(query)
        else:
            counter = counter + 1
    print("Customer done!")
    if io == 'T':
        print_nodes(greeter, "Customer")


def create_employee(greeter, io):
    counter = 0
    for employee in EMPLOYEE_list:
        if (counter != 0):
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
    if io == 'T':
        print_nodes(greeter, "Employee")


def create_item(greeter, io):
    counter = 0
    for item in ITEM_list:
        if (counter != 0):
            query = ("CREATE (n:Item {iId: " + item.iId + ", Iname: '" +
                     item.Iname + "', Sprice: " + item.Sprice + "})")
            greeter.driver.execute_query(query)
        else:
            counter = counter + 1
    print("Item done!")
    if io == 'T':
        print_nodes(greeter, "Item")


def create_oldprice(greeter, io):
    counter = 0
    for oldprice in OLDPRICE_list:
        if (counter != 0):
            query = ("CREATE (n:`Old Price` {iId: " + oldprice.iId + ", Sprice: " +
                     oldprice.Sprice + ", Sdate: '" + oldprice.Sdate + "', Edate: '" + oldprice.Edate + "'})")
            greeter.driver.execute_query(query)
        counter = counter + 1
    print("Old Price done!")
    if io == 'T':
        print_nodes(greeter, "`Old Price`")


def create_order_item(greeter, io):
    counter = 0
    for order_item in ORDER_ITEM_list:
        if (counter != 0):
            query = ("MERGE (n:`Order Item` {sId: " + order_item.sId + ", oId: " + order_item.oId + ", iId: " +
                     order_item.iId + ", Sdate: " + order_item.Icount + "})")
            greeter.driver.execute_query(query)
        counter = counter + 1
    print("Order Item done!")
    if io == 'T':
        print_nodes(greeter, "`Order Item`")


def create_order(greeter, io):
    counter = 0
    for orders in ORDERS_list:
        if (counter != 0):
            query = ("CREATE (n: Orders {oId: " + orders.oId + ", sId: " +
                     orders.sId + ", cId: " + orders.cId + ", Odate: '" + orders.Odate + "', Ddate: '" +
                     orders.Ddate + "', Amount: " + orders.Amount + "})")
            greeter.driver.execute_query(query)
        else:
            counter = counter + 1
    print("Orders done!")
    if io == 'T':
        print_nodes(greeter, "Order")


def create_store(greeter, io):
    counter = 0
    for store in STORE_list:
        if (counter != 0):
            query = ("CREATE (n: Store {sId: " + store.sId + ", Sname: '" +
                     store.Sname + "', Street: '" + store.Street + "', City: '" + store.City + "', StateAb: '" +
                     store.StateAb + "', ZipCode: '" + store.Zipcode + "', Sdate: '" + store.Sdate + "', Telno: '" +
                     store.Telno + "', URL: '" + store.URL + "'})")
            greeter.driver.execute_query(query)
        else:
            counter = counter + 1
    print("Store done!")
    if io == 'T':
        print_nodes(greeter, "Store")


def create_vendor(greeter, io):
    counter = 0
    for vendor in VENDOR_list:
        if (counter != 0):
            query = ("CREATE (n: Vendor {vId: " + vendor.vId + ", Vname: '" +
                     vendor.Vname + "', Street: '" + vendor.Street + "', City: '" + vendor.City
                     + "', StateAb: '" + vendor.StateAb + "', ZipCode: '" + vendor.Zipcode + "'})")
            greeter.driver.execute_query(query)
        else:
            counter = counter + 1
    print("Vendor done!")
    if io == 'T':
        print_nodes(greeter, "Vendor")


def create_vendor_item(greeter, io):
    counter = 0
    for vendor_item in VENDOR_ITEM_list:
        if (counter != 0):
            query = ("CREATE (n:`Vendor Item` {vId: " + vendor_item.vId + ", iId: " +
                     vendor_item.iId + ", Vprice: " + vendor_item.Vprice + "})")
            greeter.driver.execute_query(query)
        counter = counter + 1
    print("Vendor Item done!")
    if io == 'T':
        print_nodes(greeter, "`Vendor Item`")


def create_relationship_i(greeter):
    query = ("MATCH (a:Vendor), (b:`Vendor Item`), (c:Item) " +
             "WHERE a.vId = b.vId AND b.iId = c.iId " +
             "CREATE (a)-[r:SELLS]->(c) " +
             "RETURN type(r), r.name")
    greeter.driver.execute_query(query)
    print("Relationship i done.")


def create_relationship_ii(greeter):
    query = ("MATCH (a:`Vendor Item`), (b:Vendor) " +
             "WHERE a.vId = b.vId " +
             "CREATE (a)-[r:FOUND_IN]->(b) " +
             "RETURN type(r), r.name")
    greeter.driver.execute_query(query)
    print("Relationship ii done.")


def create_relationship_iii(greeter):
    query = ("MATCH (a:Orders), (b:Customer) " +
             "WHERE a.cId = b.cId " +
             "CREATE (a)-[r:BELONGS_TO]->(b) " +
             "RETURN type(r), r.name")
    greeter.driver.execute_query(query)
    print("Relationship iii done.")


def create_relationship_iv(greeter):
    query = ("MATCH (a:Orders), (b:`Order Item`), (c:Item) " +
             "WHERE a.oId = b.oId AND b.iId = c.iId " +
             "CREATE (a)-[r:CONTAINS]->(c) " +
             "RETURN type(r), r.name")
    greeter.driver.execute_query(query)
    print("Relationship iv done.")


def create_relationship_v(greeter):
    query = ("MATCH (a:`Order Item`), (b:Item) " +
             "WHERE a.iId = b.iId " +
             "CREATE (a)-[r:MATCHES]->(b) " +
             "RETURN type(r), r.name")
    greeter.driver.execute_query(query)
    print("Relationship v done.")


def create_relationship_vi(greeter):
    query = ("MATCH (a:`Employee`), (b:Store) " +
             "WHERE a.sId = b.sId " +
             "CREATE (a)-[r:WORKS_AT]->(b) " +
             "RETURN type(r), r.name")
    greeter.driver.execute_query(query)
    print("Relationship vi done.")


def create_relationship_vii(greeter):
    query = ("MATCH (a:Contract), (b:Vendor) " +
             "WHERE a.vId = b.vId " +
             "CREATE (b)-[r:HAS]->(a) " +
             "RETURN type(r), r.name")
    greeter.driver.execute_query(query)
    print("Relationship vii done.")


def create_relationship_viii(greeter):
    query = ("MATCH (a:Item), (b:`Old Price`) " +
             "WHERE a.iId = b.iId " +
             "CREATE (a)-[r:HAD]->(b) " +
             "RETURN type(r), r.name")
    greeter.driver.execute_query(query)
    print("Relationship viii done.")


def print_query(query):
    iterator = 1
    for nodes in query:
        print(str(iterator) + ':', end = " ")
        print(nodes)
        iterator = 1 + iterator


def query_i(greeter):
    query = ("MATCH (c:Customer) " +
             "WHERE c.Cname =~ 'E.*' " +
             "RETURN c.Cname, c.StateAb")
    match = greeter.driver.execute_query(query)
    print("Query i:")
    print_query(match[0])


def query_ii(greeter):
    query = ("MATCH (o:Orders), (c:Customer) " +
             "WHERE o.Amount >= 12 AND o.cId = c.cId " +
             "RETURN c.Cname")
    match = greeter.driver.execute_query(query)
    print("Query ii:")
    print_query(match[0])


def query_iii(greeter):
    query = ("MATCH (i:Item) " +
             "RETURN i.iId, i.Iname, i.Sprice " +
             "ORDER BY i.Sprice DESC " +
             "LIMIT 5")
    match = greeter.driver.execute_query(query)
    print("Query iii:")
    print_query(match[0])


def query_vi(greeter):
    query = ("MATCH (o:Orders) " +
             "UNWIND o.Odate as Odate " +
             "RETURN o.Odate, sum(o.Amount) as `o.Amount`")
    match = greeter.driver.execute_query(query)
    print("Query iv:")
    print_query(match[0])



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

    # The only reason I am using a switch statement is because older versions of python do not support it.
    if (fname == "CONTRACT"):
        read_CONTRACT(data)
    elif (fname == "CUSTOMER"):
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

    def __init__(self, uri, AUTH):
        self.driver = GraphDatabase.driver(uri, auth=(AUTH))

    def close(self):
        self.driver.close()


def main():
    URI = "bolt://44.201.15.215:7687"
    AUTH = ("neo4j", "envelope-partition-cents")

    greeter = DBDriver(URI, AUTH)
    #greeter.driver.execute_query("MATCH (n) DETACH DELETE n")

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()

    skip = input("Connection Verified. Press Enter to read data:")
    if(skip != 'skip'):
        greeter.driver.execute_query("MATCH (n) DETACH DELETE n")
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
        io = input("Press 'T' enable node printing: ")

        create_contract(greeter, io)
        create_customer(greeter, io)
        create_employee(greeter, io)
        create_item(greeter, io)
        create_oldprice(greeter, io)
        create_order_item(greeter, io)
        create_order(greeter, io)
        create_store(greeter, io)
        create_vendor(greeter, io)
        create_vendor_item(greeter, io)

        print("Data Creation complete.")
        io = input("Press Enter to create Relationships: ")
        create_relationship_i(greeter)
        create_relationship_ii(greeter)
        create_relationship_iii(greeter)
        create_relationship_iv(greeter)
        create_relationship_v(greeter)
        create_relationship_vi(greeter)
        create_relationship_vii(greeter)
        create_relationship_viii(greeter)
        print("Relationsips done.")
    io = input("Press Enter to run Queries: ")

    query_i(greeter)
    query_ii(greeter)
    query_iii(greeter)
    query_iv(greeter)
    query_v(greeter)


    greeter.close()


main()
