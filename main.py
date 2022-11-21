#program that reads from a text file and outputs users who have a prescription based on ascending order of their record date
from datetime import datetime

year = []
month = []
day = []
date = []
cdsaEntry=[]
masterDate = []
with open ("pharmacy_list.txt",'r') as f:
    for line in f:
        if "No" in line:
            continue
        else:
            cdsaEntry.append(line.split(','))


cdsaEntry.sort(key=lambda entry: datetime.fromisoformat(entry[2][1:11]))

print("{:<20} | {:<15} | {:<20} | {:<15}".format('Patient Name', 'Drug ID', 'Prescription Date', 'Name of CDSA'))
print(80 * '-')

for entry in cdsaEntry:
    print("{:<20} | {:<15} | {:<20} | {:<15}".format(entry[0], entry[1], entry[2], entry[4]))

opium = 0
hydrocone = 0
etorphine = 0
metopon = 0
morphine = 0
ethylmorphine = 0
apomorphine = 0
nicocodine = 0
oxycodone = 0
pethidine = 0
for entry in cdsaEntry:
    if " Opium" in entry:
        opium = opium + 1
    if " Hydrocone" in entry:
        hydrocone += 1
    if " Etorphine" in entry:
        etorphine += 1
    if " Metopon" in entry:
        metopon += 1
    if " Morphine" in entry:
        morphine += 1
    if " Ethylmorphine" in entry:
        ethylmorphine += 1
    if " Apomorphine" in entry:
        apomorphine += 1
    if " Nicocodine" in entry:
        nicocodine += 1
    if " Oxycodone" in entry:
        oxycodone += 1
    if " Pethidine" in entry:
        pethidine += 1

substance = 0
substance = len(cdsaEntry)

print("\nTotal Prescriptions with CDSA substances :", substance)
print("Opium:", opium)
print("Hydrocone:", hydrocone)
print("Etorphine:", etorphine)
print("Metopon:", metopon)
print("Morphine:", morphine)
print("Ethylmorphine:", ethylmorphine)
print("Apomorphine:", apomorphine)
print("Nicocodine:", nicocodine)
print("Oxycodone:", oxycodone)
print("Pethidine:", pethidine)