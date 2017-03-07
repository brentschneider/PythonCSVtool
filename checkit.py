import csv

##################################################
# 💌 Email csv list comparison tool
# 👋 Author: Brent @webmedic
# 🔥 Convert array to string, save just strings
# 🔥 Check variable lenth of colums
# 🔥 Convert hard code path to input
##################################################

# Opens File for result output
f = open('theResult.csv', 'w')

# Opens File serving as your "Dictonary" file to compare against
with open('followupDataList.csv', 'rU') as csvfile1:
# Opens file containing ALL data
    with open ("theOrigionalList.csv", "rU") as csvfile2:
        reader1 = [row for row in csv.reader(csvfile1.read().splitlines())]
        reader2 = [row for row in csv.reader(csvfile2.read().splitlines())]
        rows1_col_a = [row[0] for row in reader1]
        rows2 = [row for row in reader2]
        only_b = []

        for row in rows2:
            if row[0] not in rows1_col_a:
                only_b.append(row)
        print (repr(only_b)) # Because Feedback feels good

        f.write(str.strip('[' + str(only_b) + ']')) # This section needs cleaning up a bit see notes
        f.close() # you can omit in most cases as the destructor will call it
