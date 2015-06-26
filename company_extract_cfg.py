####this is the cfg file for company extract###
import os
import sys
import subprocess
import random
import linecache
reload(sys)
sys.setdefaultencoding('gbk')

format_address = open("loc_words.txt",'r').readlines()
format_mess = ['1','2','3','4','5','6','7','8','9','0','!',',','|']
def generate_test_data():
    FILE_PATH = sys.path[0]
    result_log_info=open("test.csv","w")
    result_log_info.truncate()
    '''cmd = "sort -R building_split.csv | head -20"  
    data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True) 
    result_log_info.write(data.stdout.read().strip("\n")) 
    result_log_info.close()'''
    for i in range(1000):
        random_num = random.randrange(1,1000000, 1)
        result_log_info.write(linecache.getline("building_split.csv",random_num))
        
if __name__ == '__main__':
    generate_test_data()    
