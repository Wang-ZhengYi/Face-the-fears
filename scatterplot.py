#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
created on Jan.,2020

@Author:
'''

from def_import import *

def readCsv(file_name):
    with open(file_name,'r') as f:
      rander=csv.reader(f)
    return rander


def TOD0(csv_data,k):
    k = np.int(k)
    o_p = csv_data[8][k],csv_data[9][k]
    d_p = np.array([np.float64(csv_data[10][k]),np.float64(csv_data[11][k])])
    t = np.float64(csv_data[5][k])
    plt.scatter(o_p,'r')
    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
	file_name = 'csvdata/fullevents.csv'
	csv_data = readCsv(file_name)
	print(csv_data[7])
