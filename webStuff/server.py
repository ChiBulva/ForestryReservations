from flask import Flask, render_template, url_for, request
import os
import csv
from datetime import datetime, date

app = Flask(__name__)

# CSV functions
################################################################################################################################################################
# -                                     1       2       3       4       5         6       7       8       9       10
# - Files:  HelpdeskItems           ( Number, Item,  ItemType,Status,Description )
# -         CheckedoutandReserved   ( Item,   User,    In,    Out,    Dest,     Desc,  Status )
# -         OnidUsernames           ( Onid )
# -
# - Needs:  Buttons: ReserveItem
# -

#############################################################################################################################
# Header function that catch new items And errors
#############################################################################################################################

def checkoutitem(Item, User, In, Out, DateIn, DateOut, Destination, Description, Status):
    DesiredStatus = "out"

    #TODO: ERROR checking
    #Error checking done here
    #
    InNum = timetoint(In)
    OutNum = timetoint(Out)
    DateNum = datetoint(DateIn,DateOut)

    #print(DateIn)
    #print(DateOut)

    d1 = datetime.strptime(DateIn, "%Y-%m-%d").weekday()
    d2 = datetime.strptime(DateOut, "%Y-%m-%d").weekday()

    #print("in: "+str(d1))
    #print("out: "+str(d2))

    if(DateNum>14 or d1>=5 or d2>=5):
        if(d1>=5):
            print("Error, Cannot Checkin on Saturday or Sunday")
            return "Error, Cannot Checkin on Saturday or Sunday"
        elif(d2>=5):
            print("Error, Cannot Checkout on Saturday or Sunday")
            return "Error, Cannot Checkout on Saturday or Sunday"
        else:
            print("Error, cannot reserve items for more than 14 days")
            return "Error, cannot reserve items for more than 14 days. Currently "+str(DateNum)+" days long"
    else:
        #print(DateNum)

        if(Status!="new"):
            #print("   NOT ITEMNEW checkoutitem")
            changeStatus(DesiredStatus, Item)
            delRowFromCheckedOutAndReserved(Item, User, "reserved")
            addRowToCheckedOutAndReserved(Item, User, In, Out, DateIn, DateOut, Destination, Description, DesiredStatus)
        return 0

def reserveitem(Item, User, In, Out, DateIn, DateOut, Destination, Description, Status):
    DesiredStatus = "reserved"

    #TODO: ERROR checking
    #Error checking done here
    #
    InNum = timetoint(In)
    OutNum = timetoint(Out)
    DateNum = datetoint(DateIn,DateOut)

    d1 = datetime.strptime(DateIn, "%Y-%m-%d").weekday()
    d2 = datetime.strptime(DateOut, "%Y-%m-%d").weekday()
    if(DateNum>14 or d1>=5 or d2>=5):
        if(d1>=5):
            print("Error, Cannot Checkin on Saturday or Sunday")
            return "Error, Cannot Checkin on Saturday or Sunday"
        elif(d2>=5):
            print("Error, Cannot Checkout on Saturday or Sunday")
            return "Error, Cannot Checkout on Saturday or Sunday"
        else:
            print("Error, cannot reserve items for more than 14 days")
            return "Error, cannot reserve items for more than 14 days. Currently "+str(DateNum)+" days long"
    else:
        #print(DateNum)

        if(Status!="new"):
            #print("   NOT ITEMNEW reserveitem")
            changeStatus(DesiredStatus, Item)
            delRowFromCheckedOutAndReserved(Item, User, "out")
            addRowToCheckedOutAndReserved(Item, User, In, Out, DateIn, DateOut, Destination, Description, DesiredStatus)
        return 0

def checkinitem(Item, User, Status):
    DesiredStatus = "in"
    #print(User)
    #print(Item)
    if(Status!="new"):
        changeStatus(DesiredStatus, Item)
    delRowFromCheckedOutAndReserved(Item, User, DesiredStatus)

def reservecheckout(Item, User):
    DesiredStatus = "out"
    changeStatus(DesiredStatus, Item)

def cancelitem(Item, User, Status):
    DesiredStatus = "in"
    if(Status!="new"):
        #print("   NOT ITEMNEW cancelitem")
        changeStatus(DesiredStatus, Item)
    delRowFromCheckedOutAndReserved(Item, User, DesiredStatus)

#############################################################################################################################
# Controllers for different checkout/checkin/reserve options
#############################################################################################################################

# +  Actual manipulation of CSV files
# +
def changeStatus(DesiredStatus, Item):
    inputfile = csv.reader(open('./static/storage/HelpdeskItems.csv','r', encoding='utf-8'))
    #outfile =
    newFileArray = []
    for row in inputfile:
        if(len(row)==0):
            #print(row)
            pass
        elif(row[1]==Item):
            newFileArray.append([(str(row[0])),(str(row[1])),(str(row[2])),(str(DesiredStatus)),(str(row[4]))])
        else:
            newFileArray.append(row)

    outfile = csv.writer(open('./static/storage/HelpdeskItems.csv','w'))
    for row in newFileArray:
        if(len(row)==0):
            #print(row)
            pass
        else:
            #print(row)
            outfile.writerow(row)

def ResToOut(DesiredStatus, Item):
    #print("INSIDE OMG")
    inputfile = csv.reader(open('./static/storage/HelpdeskItems.csv','r', encoding='utf-8'))
    #outfile =
    newFileArray = []
    for row in inputfile:
        if(len(row)==0):
            #print(row)
            pass
        elif(row[1]==Item):
            newFileArray.append([(str(row[0])),(str(row[1])),(str(row[2])),(str(DesiredStatus)),(str(row[4]))])
        else:
            newFileArray.append(row)

    outfile = csv.writer(open('./static/storage/HelpdeskItems.csv','w'))
    for row in newFileArray:
        if(len(row)==0):
            pass
        else:
            #print(row)
            outfile.writerow(row)

    inputfile = csv.reader(open('./static/storage/CheckedoutandReserved.csv','r', encoding='utf-8'))
    #outfile =
    newFileArray = []
    for row in inputfile:
        if(len(row)==0):
            pass
            #print(row)
        elif(row[0]==Item):
            newFileArray.append([(str(row[0])),(str(row[1])),(str(row[2])),(str(row[3])),(str(row[4])),(str(row[5])),(str(row[6])),(str(row[7])),(str(DesiredStatus))])
        else:
            newFileArray.append(row)

    outfile = csv.writer(open('./static/storage/CheckedoutandReserved.csv','w'))
    for row in newFileArray:
        if(len(row)==0):
            pass
            #print(row)
        else:
            #print(row)
            outfile.writerow(row)
# +
# +
def addRowToCheckedOutAndReserved(Item, User, TimeIn, TimeOut, DateIn, DateOut, Dest, Desc, DesiredStatus):
    inputfile = csv.reader(open('./static/storage/CheckedoutandReserved.csv','r', encoding='utf-8'))
    newFileArray = []
    timetoint
    for row in inputfile:
        if(len(row)==0):
            #print(row)
            pass
        else:
            newFileArray.append(row)

    newFileArray.append([Item, User, TimeIn, TimeOut, DateIn, DateOut, Dest, Desc, DesiredStatus])

    outfile = csv.writer(open('./static/storage/CheckedoutandReserved.csv','w'))
    for row in newFileArray:
        if(len(row)==0):
            pass
            #print(row)
        else:
            #print(row)
            outfile.writerow(row)
# +
# +
def delRowFromCheckedOutAndReserved(Item, User,  DesiredStatus):
    inputfile = csv.reader(open('./static/storage/CheckedoutandReserved.csv','r', encoding='utf-8'))
    newFileArray = []
    for row in inputfile:
        if(len(row)==0):
            pass
        elif(row[1]==User and row[0]==Item):
            pass
            #print("Skipped: "+str(User))
        else:
            newFileArray.append(row)

    outfile = csv.writer(open('./static/storage/CheckedoutandReserved.csv','w'))
    for row in newFileArray:
        #print(row)
        outfile.writerow(row)

def timetoint(integer):
    if(integer=='8:00 AM'):
        return '8'
    elif(integer=='9:00 AM'):
        return '9'
    elif(integer=='10:00 AM'):
        return '10'
    elif(integer=='11:00 AM'):
        return '11'
    elif(integer=='12:00 PM'):
        return '12'
    elif(integer=='1:00 PM'):
        return '1'
    elif(integer=='2:00 PM'):
        return '2'
    elif(integer=='3:00 PM'):
        return '3'
    elif(integer=='4:00 PM'):
        return '4'
    elif(integer=='5:00 PM'):
        return '5'

def datetoint(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")

    #print("Days time")
    #print(abs((d2 - d1).days))
    return abs((d2 - d1).days)

#############################################################################################################################
# Functions to mamipulate CSV files
#############################################################################################################################

#Returns list of csv rows
#
def csvRowsList(filename):
    with open("./static/storage/test.csv") as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
    return readCSV

#Returns specific row of csv
#
def csvSpecificRows(filename, x):
    with open("./static/storage/test.csv") as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
    return readCSV[x]

# Turns a csv into a dictionary for easier display
#
def csvtodict(filename):
    passreader = csv.DictReader(open(filename, 'r'))
    dict_list = []

    for line in passreader:
        #print(line)
        dict_list.append(line)
    return dict_list

def Reserve():
    print("RESERVED")

#############################################################################################################################
# Main page for the application
#############################################################################################################################

#Main page
#
@app.route('/', methods=['GET', 'POST', 'Item', 'User', 'lenInventoryList', 'TimeIn', 'TimeOut', 'DateIn', 'DateOut', 'Destination', 'Description', 'Rescheck', 'CheckoutTrigger', 'ReserveTrigger', 'CheckinTrigger', 'CheckOutRes', 'CancelRes', 'Status'])
def Reservations():
    if request.method == 'POST':
    	data = request.form
    else:
    	data = request.args

    Item = data.get('Item')
    User = data.get('User')

    #Variables from HTML-----------
    #------------------------------

    TimeIn = data.get('TimeIn')
    TimeOut = data.get('TimeOut')
    Destination = data.get('Destination')
    Description = data.get('Description')
    CheckoutTrigger = data.get('CheckoutTrigger')
    ReserveTrigger = data.get('ReserveTrigger')
    CheckinTrigger = data.get('CheckinTrigger')
    CheckOutRes = data.get('CheckOutRes')
    DateIn = data.get('DateIn')
    DateOut = data.get('DateOut')
    CancelRes = data.get('CancelRes')
    Status = data.get('Status')

    Rescheck = 1

    print("|>"+str(DateIn)+"<|")
    print("|>"+str(DateOut)+"<|")

    CurrentDate = str(datetime.now().year)+"-"+str(datetime.now().month)+"-"+str(datetime.now().day)

    if(DateIn=='' or DateIn=='None' or DateIn==0):
        DateIn = CurrentDate
    if(DateOut=='' or DateOut=='None' or DateOut==0):
        DateOut = CurrentDate

    print(DateIn)
    print(DateOut)
    #Manipulates CSV files---------
    #------------------------------
    ErrorOrNot = 'None'

    if(CheckoutTrigger == 'Checkout Item'):
        ErrorOrNot = checkoutitem(Item, User, TimeIn, TimeOut, DateIn, DateOut, Destination, Description, Status)
        if(ErrorOrNot == 'None' or ErrorOrNot == 0):
            Item = 'None'
            #User = 'None'

    elif(CheckinTrigger == 'Check-In'):
        checkinitem(Item, User, Status)
        Item = 'None'
        #User = 'None'

    elif(CheckOutRes == 'Check Out'):
        ResToOut("out", Item)
        Item = 'None'
        #User = 'None'

    elif(ReserveTrigger == 'Reserve Item'):
        ErrorOrNot = reserveitem(Item, User, TimeIn, TimeOut, DateIn, DateOut, Destination, Description, Status)
        if(ErrorOrNot == 'None' or ErrorOrNot == 0):
            Item = 'None'
            #User = 'None'

    elif(CancelRes == 'Cancel'):
        cancelitem(Item, User, Status)
        Item = 'None'
        #User = 'None'

    if(Item!=None and Item!='None') and (User!=None and User!='None'):
        Rescheck = 0;

    #Grabs newest csv data after manipulation--
    #------------------------------------------

    #fetches current cvs for Inventry
    filename="./static/storage/HelpdeskItems.csv"
    InventoryList = csvtodict(filename)

    #fetches current cvs for REserved Item and Checked out Item
    filename="./static/storage/CheckedoutandReserved.csv"
    ReservedList = csvtodict(filename)

    #fetches current cvs for Inventry
    filename="./static/storage/OnidUsernames.csv"
    OnidList = csvtodict(filename)
    #print(OnidList)

    Status = 'None'
    #Calls the HTML and css templates
    return render_template('Homepage.html',
        CurrentDate=CurrentDate,
        ErrorOrNot=ErrorOrNot,
        InventoryList=InventoryList,
        OnidList=OnidList,
        ReservedList=ReservedList,
        Item=Item,
        User=User,
        TimeIn=TimeIn,
        TimeOut=TimeOut,
        Destination=Destination,
        Description=Description,
        CheckoutTrigger=CheckoutTrigger,
        ReserveTrigger=ReserveTrigger,
        CheckinTrigger=CheckinTrigger,
        CheckOutRes=CheckOutRes,
        DateIn=DateIn,
        DateOut=DateOut,
        CancelRes=CancelRes,
        #Status=Status,
        Rescheck=Rescheck)

#############################################################################################################################
# Allows for user to update code while server is running
#############################################################################################################################

#Found at URL: http://flask.pocoo.org/snippets/40/
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

#############################################################################################################################
# Main Function
#############################################################################################################################

if __name__ == '__main__':
	app.run(debug=True, port=5001) #Set Port and run app
