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

def pass_stats1(file_name,nrow):
    dataSet=[] 
    with open(file_name,'r') as file: 
        csvReader=csv.reader(file) 
        data1 = list([row[nrow] for row in csvReader])
        file.close()
    return data1

def tex_count(file_name,nrow):
    dataSet=[] 
    with open(file_name,'r') as file: 
        csvReader=csv.reader(file) 
        data = list([row[nrow] for row in csvReader])
        file.close()
        tex_count0 = Counter(data)
    return tex_count0


if __name__ == '__main__':
    file_name0 = 'csvdata/fullevents.csv' 
    file_name = 'csvdata/passingevents.csv'
    # data0,data1 = pass_stats0(file_name),pass_stats1(file_name)
    a = tex_count(file_name0,6)
    print(a)