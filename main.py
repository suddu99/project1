# import libraries
import csv
import xml.etree.ElementTree as ET
import logging
import pandas as pd
import xml.etree.ElementTree as newXML

# load data into file data
df = pd.read_csv("data.csv")

# filter the duplicate values
df1 = df.drop_duplicates(subset=['Mobile Number', 'Service Indication'], keep="first")

# Copy the filtered data to file data1
df2 = df1.to_csv("data1.csv", index=False)

# Creating a log file of filename = logfile.log
logging.basicConfig(filename='logfile.log', level=logging.INFO ,
                    format='%(asctime)s %(levelname)s-%(message)s''\n')

# function to search by service Indication
def searchByserviceIndication(num):
    global sr_indication
    lst = []
    for i in range(0, num):
        sr_indication = input("Enter the service indication")
        lst.append(sr_indication)

    csv_file = csv.reader(open("data1.csv", "r"))
    if num == 1:
        for row in csv_file:
            if sr_indication == row[2]:
                logging.info(row)
    elif num > 1:
        for row in csv_file:
            if row[2] in lst:
                logging.info(row)

# function to search by mobile number
def searchBynumber():
    mb_num = input("Enter the Mobile Number")
    csv_file = csv.reader(open("data1.csv", "r"))
    for row in csv_file:
        if mb_num == row[0]:
            logging.info(row)

# function to sort according to batchsize
def batchSize():
    # count = 0
    tree = ET.parse('data.xml')
    c = []
    root = tree.getroot()
    root1 = newXML.Element("Audit")
    for i in range(batchsize):
        print('\n')
        c.append(newXML.Element("auditSubscribers"))
        root1.append(c[i])
        sc = []
        count = 0
        for j in root[i]:
            # print(j.tag, j.text)
            sc.append(newXML.SubElement(c[i], j.tag))
            sc[count].text = j.text
            count = count + 1  # count used becauses i is not an integer i.e it is an XML element
    tree1 = newXML.ElementTree(root1)
    with open("data1.xml", "wb") as files:
        tree1.write(files)

# Main Function
print("Enter 1 to search by service indication ")
print("Enter 2 to search by mobile number ")
print("Enter 3 to sort xml file according to batchsize ")
src = int(input("Enter here : "))

if src == 1:
    num = int(input("Enter number of service indications"))
    searchByserviceIndication(num)
elif src == 2:
    searchBynumber()
elif src == 3:
    batchsize = int(input("Enter the batch size : "))
    if batchsize <= 8:
        batchSize()
    else:
        logging.info("Invalid Input ")
else:
    logging.info("Invalid input ")
