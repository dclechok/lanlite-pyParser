import csv

lanliteDict = {}
with open('lanlite-ips.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    counter = 0
    for row in spamreader:
        # print(row["Version"])
        if row["Version"].find('lanlite') != -1:
            lanliteDict.update({ row["IP address"]: "Lanlite"})

with open('lanlites.csv', 'w', newline='') as csvfile:
    fieldnames = ['IP Address', 'Lanlite']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for key in lanliteDict:
        writer.writerow({ "IP Address": key, "Lanlite": lanliteDict[key] })