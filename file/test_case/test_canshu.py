# -*-coding:utf-8-*-
import pytest
import os,sys
sys.path.append('..')
from data.read_csv import *

class Test001:


    @pytest.mark.parametrize('a',readcsv('../data/file.csv'))
    def test001(self,a):
        title,header,path,method,json,ex=a
        print(title)
        print(header)
        # print(a)
if __name__ == '__main__':
    pytest.main()