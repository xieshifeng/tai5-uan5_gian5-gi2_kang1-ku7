'''
Created on 2013/3/1

@author: Ihc
'''
from 剖析相關工具.剖析工具 import 剖析工具
工具=剖析工具()
結果=工具.剖析('我們要下班，我和他想回家，你們兩個想睡覺。')
結果=工具.剖析('我覺得我做了一個假的作品')
print(結果)

