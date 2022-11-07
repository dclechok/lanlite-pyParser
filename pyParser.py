import csv

lanliteDict = {}
with open('lanlite-ips.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    # build a dictionary of ip addresses, and whether or not they are lanlite
    for row in spamreader:
        # print(row["Version"])
        if row["Version"].find('lanlite') != -1:
            lanliteDict.update({ row["IP address"]: "Lanlite"})

# build a new CSV file with key/values within dictionary
with open('lanlites.csv', 'w', newline='') as csvfile:
    fieldnames = ['IP Address', 'Lanlite']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for key in lanliteDict:
        writer.writerow({ "IP Address": key, "Lanlite": lanliteDict[key] })