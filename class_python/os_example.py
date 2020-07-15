import os

print(os.path)

'''출력내용
<module 'ntpath' from 'C:\\Users\\평일_취업반_이시형\\AppData\\Local\\Programs\\Python\\Python37\\lib\\ntpath.py'>
'''

print(os.cpu_count())   ## 8
print(os.getlogin())    ## 평일_취업반_이시형
os.mkdir('경로명', mode='', dir_fd='')