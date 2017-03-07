# -*- coding: utf-8 -*-

import csv
import sys
import Tkinter, tkFileDialog
import os

#/---------------------------------------------------------------
#  Email csv list comparison tool
#
#  👋 Author: Brent @webmedic
#  👥 Collaborators : James & Ralf
#
#  TODO:
#  📌 🔥 Convert hard coded path to dynamic file location / open from directory
#  📌 1 of 2 Curent state is singe colum mode, expand to allow for additional rows
#  📌 2 of 2 Set acolums for key values to check against, such as email or ID
#
#/---------------------------------------------------------------


#/---------------------------------------------------------------
# Select the file for output 📌 see convert to dynamic file location

root = Tkinter.Tk()
root.withdraw()
''
filename = tkFileDialog.askopenfilename(parent=root,title='Pick a file')

if filename != None:
    f = open(str(filename), 'w')

 # Select the file hardcode
f = open('theresult2.csv', 'w')

#/---------------------------------------------------------------
# Opens File serving as your "Dictonary" file to compare against

with open('Origional.csv', 'ra') as csvfile1:

#/---------------------------------------------------------------
# Opens file containing data to remove from Origional

    with open ("2ndrun.csv", "ra") as csvfile2:
        reader1 = [row for row in csv.reader(csvfile1.read().splitlines())]
        reader2 = [row for row in csv.reader(csvfile2.read().splitlines())]
        rows1_col_a = [row[0] for row in reader1]
        rows2 = [row for row in reader2]
        only_b = []

        # set counter
        lucky = 0

        for row in rows2:
            if row[0] not in rows1_col_a:
                lucky = lucky + 1
                only_b.append(row)
                print (only_b[lucky-1][0] + ",") # Because Feedback feels good

                f.write(only_b[lucky-1][0] + "," + "\n") # This section needs cleaning up a bit see notes
        f.close() # you can omit in most cases as the destructor will call it
