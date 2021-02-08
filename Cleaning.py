import pandas as pd
import numpy as np

firstName = []
lastName = []
fields = ['NAME ', 'EMAIL ']
toCopy = pd.read_csv("""NAME HERE""", header=None)


def splitName(item):
    item = item.split()
    first = item[0]
    first.capitalize()
    firstName.append(first)
    last = item[len(item)-1]
    if '(' in last:
        last = item[1] + " " + item[2]
    last.capitalize()
    lastName.append(last)


emails = []
def email(item):
    emails.append(item)

toCopy = toCopy.dropna()

"""
toCopy = toCopy.rename(columns={'EMAIL ': 'EMAIL'})
toCopy = toCopy.rename(columns={'NAME ': 'NAME'})
"""


toCopy[0].map(splitName)
toCopy[1].map(email)

DF = pd.DataFrame(zip(firstName, lastName, emails))

DF.to_csv('jul27.csv')