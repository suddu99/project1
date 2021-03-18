# import libraries
import pandas as pd
import csv

# load data into file data
df = pd.read_csv("data.csv")

# filter the duplicate values
df1 = df.drop_duplicates(subset=['Mobile Number', 'Service Indication'], keep="first")

# Copy the filtered data to file data1
df2 = df1.to_csv("data1.csv", index=False)


# function to search by service Indication
def searchByserviceIndication(num):
    lst = []
    for i in range(0,num):
        sr_indication = input("Enter the service indication")
        lst.append(sr_indication)

    csv_file = csv.reader(open("data1.csv", "r"))
    if num == 1:
        for row in csv_file:
            if sr_indication == row[2]:
                print(row)
    elif num > 1:
        for row in csv_file:
            if row[2] in lst:
                print(row)

# function to search by mobile number
def searchBynumber():
    mb_num = input("Enter the Mobile Number")
    csv_file = csv.reader(open("data1.csv", "r"))
    for row in csv_file:
        if mb_num == row[0]:
            print(row)

print("Enter 1 to search by service indication ")
print("Enter 2 to search by mobile number ")
src = int(input("Enter here : "))

if src == 1:
    num = int(input("Enter number of service indications"))
    searchByserviceIndication(num)
elif src == 2:
    searchBynumber()
else:
    print("Invalid input")
