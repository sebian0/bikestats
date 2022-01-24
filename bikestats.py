#imports
from cgitb import text
from fileinput import filename
import os
import openpyxl
import datetime
# import froms
from openpyxl import Workbook
#load
Workbook_obj = openpyxl.load_workbook(r"<full file path to excel sheet.xlsx>")
sheet_obj = Workbook_obj.active
#Date/Time data
DATE = input("Date: ")
col1 = DATE

#Miles data
MILES = input("Miles: ")
col2 = MILES

# Time length data
TIME = input("How long did you ride? ")
col3 = TIME

# Heart rate data
HTRATE = input("Average Heartrate ")
col4 = HTRATE

sheet_obj.append([col1, col2, col3, col4])
Workbook_obj.save("<full file path to excel sheet.xlsx>")

