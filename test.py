from def_import import *


def colorset(tex):
    if tex == "Simple pass":
        return 'blue'
    if tex ==  'Head pass':
        return 'black'
    if tex == 'High pass':
        return 'yellow'
    if tex == 'Launch':
        return 'green'
    if tex == 'Cross':
        return 'red'
    if tex == 'Smart pass':
        return 'oringe'
    if tex == 'Hand pass':
        return 'pink'
    else:
        return 'blue'

def readCsv(file_name):
    dataSet=[] 
    with open(file_name,'r') as file: 
        csvReader=csv.reader(file) 
        a = list(csvReader)
        file.close()
    return a


if __name__ == '__main__':
    file_name = 'csvdata/passingevents.csv'
    data = readCsv(file_name)
    MatchID = []
    MatchID = data[0]
    a = MatchID[5]*1.

    # print(data[1][1])
    print(a)
