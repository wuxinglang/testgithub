# -*-coding:utf-8-*-
import csv
import xlrd

#
# def readcsv(filename):
#     #
#     with open(filename, 'r') as f:
#
#         reader =csv.reader(f)    # 为了跳过首行
#         resurt=list(reader)
#         print(resurt)
#     return resurt

def readcsv(filename):

    data = xlrd.open_workbook(filename, 'rb')
    print(data)
    return data

readcsv('file.xltx')
