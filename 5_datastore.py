# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


"""
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

"""


datastore = {
    "medical": [
        {"room-number": 100, "use": "reception", "sq-ft": 50, "price": 75},
        {"room-number": 101, "use": "waiting", "sq-ft": 250, "price": 75},
        {"room-number": 102, "use": "examination", "sq-ft": 125, "price": 150},
        {"room-number": 103, "use": "examination", "sq-ft": 125, "price": 150},
        {"room-number": 104, "use": "office", "sq-ft": 150, "price": 100},
    ]
}

import csv

# OPENING THE CSV
retail_space = open("retail_space.csv", "w", newline="")
writer = csv.writer(retail_space)
# WRITING THE ROW FOR HEADER
writer.writerow(["room-number", "use", "sq-ft", "price"])
# ACCESSING VALUES IN MEDICAL DICTIONARY:
for medical in datastore["medical"]:
    writer.writerow(
        [medical["room-number"], medical["use"], medical["sq-ft"], medical["price"]]
    )
# CLOSE CSV
retail_space.close()

# USING THE DOT VALUES METHOD (INDEX VALUE) CAN BE A LOT MORE EFFICIENT

# IN CLASS EXAMPLE
# outfile=open('retail_space.csv', 'w')
# outfile.write('room-number, use, sq-ft, price\n')

# list = datastore['medical']

# for each in list:
#    use = each['use']
#    sq = each['sq-ft']
#    price = each['price']

#    outfile.write(str(rn) + ',' + use + ',' + str(sq) + ',' + str(price) + '\n')

# outfile.close()
