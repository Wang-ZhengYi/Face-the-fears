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



if __name__ == '__main__':
	file_name = 'csvdata/fullevents.csv'
	csv_data = readCsv(file_name)
	pitch.createPitch()
