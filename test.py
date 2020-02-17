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

def pass_stats0(file_name):
    dataSet=[] 
    with open(file_name,'r') as file: 
        csvReader=csv.reader(file) 
        data0 = list(csvReader)
        file.close()
    return data0

def pass_stats1(file_name):
    dataSet=[] 
    with open(file_name,'r') as file: 
        csvReader=csv.reader(file) 
        data1 = list([row[0] for row in csvReader])
        file.close()
    return data1

if __name__ == '__main__':
    file_name = 'csvdata/passingevents.csv'
    data0,data1 = pass_stats0(file_name),pass_stats1(file_name)

    # b = []
    # b = ['1',1,1,11,1,2,4,33,3,1,4]
    # a = b.count(1)
    M =1
    a = data1.count('{}'.format(M))
    b = data0[1]
    # print(data[1][1])
    print(a)
    print(b)
