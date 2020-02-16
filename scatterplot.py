#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
created on Jan.,2020

@Author:
'''

from def_import import *


def readCsv(file_name):
    dataSet=[] 
    with open(filename,'r') as file: 
        csvReader=csv.reader(file) 
    for line in csvReader: 
        dataSet.append(line) 
    return dataSet


if __name__ == '__main__':
	file_name = 'csvdata/fullevents.csv'
	csv_data = readCsv(file_name)
	n = 150
	x = np.random.rand(n,3)
	c = np.random.rand(n,3)
    print(x.shape)
	plt.scatter(x[:,0], x[:,1], s=x[:,2]*500, alpha=0.5, color=c)
	# pitch.createPitch()
	plt.show()