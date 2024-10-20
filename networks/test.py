import csv

def get_preferences():
    node_list = []
    with open('preference.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar='"')
        for row in spamreader:
            node_list.append(row[1:None])
    return node_list

node_list = get_preferences()
print(node_list)