import pandas as pd
import numpy as np
"""
Reading in Emailcsv
"""


toCopy = pd.read_csv("FILE NAME HERE ")


toCopy = toCopy.rename(columns={'EMAILS ': 'EMAILS'})
firstName = []
lastName = []
email = []
blank = " "

def splitName(item):
    item = item.split()
    if len(item)>1:
        item[0].capitalize()
        item[1].capitalize()
        firstName.append(item[0])
        lastName.append(item[1])
        email.append(item[len(item)-1])
    else:
        firstName.append(blank)
        lastName.append(blank)
        email.append(item[0])


toCopy['EMAILS'].map(splitName)

print(email)
email = [i[1:-2] for i in email]

DF = pd.DataFrame(zip(firstName, lastName, email))
DF.to_csv('FILE_NAME')