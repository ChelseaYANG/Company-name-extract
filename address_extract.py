#encoding=gbk
import os
import sys
import re
import jieba
import company_extract_cfg
reload(sys)
sys.setdefaultencoding('gbk')

class COMPANY_EXTRACT():
    global format_mess,format_address 
    format_mess = company_extract_cfg.format_mess
    format_address = company_extract_cfg.format_address
    def raw_extract(self):
        #company_extract_cfg.generate_test_data()
        file = open("building_split.csv", "r")
        result_info = open("EXTRACT_RESULT.txt","w")
        result_data = []
        while True:
            line=file.readline()

            if line:
            #for line in file:
                # begin the interation by go through each line
                # poi labeled as 15
                temp_data = line
                temp_data2 = line
                if "|15!" in line:

                    # has 15 not 26
                    if "|26" not in line:
                        
                        if line.count("|15!") >= 1:
                            for i in range(line.count("|15!")):
                                line = temp_data2
                                if "!" in line.split("|15!")[i]:
                                    #print "$$$",line.split("|15!")[i]
                                    line = line.split("|15!")[i].split("!")[-1]
                                else:
                                    line = line.split("|15!")[i]
                                line = unicode(line,"gbk")
                                temp = re.compile(u"[\u4e00-\u9fa5]{1}")
                                line = temp.findall(line)
                                #if it is a company
                                if "司" in line:
                                    # if data is clean 
                                    if "区" not in line or "街" not in line or "路" not in line:
                                        #print "@@@" + ''.join(line)
                                        #result_data.append(''.join(line)+"\n")
                                        temp_data  = temp_data.strip("\n") + "\t" +''.join(line)+"\n"
                                        result_info.write(temp_data)
                                        
                                    #in case has dirty words
                                    else:
                                        for each_word in format_address:
                                            each_word = unicode(each_word,"gbk")
                                            temp_each_word = re.compile(u"[\u4e00-\u9fa5]{1}")
                                            each_word = ''.join(temp_each_word.findall(each_word))                                        
                                            #line is a list
                                            if ''.join(line).rfind(each_word) is not -1:
                                            #if ''.join(format_address).rfind(each_string) is not -1:                 
                                                #line = ''.join(line)[''.join(line).rfind(each_string)+1:]
                                                line = ''.join(line)[''.join(line).rfind(each_word)+len(each_word):]
                                            else:
                                                line = ''.join(line)
                                                print ''.join(line)
                                                #result_data.append(''.join(line)+"\n")
                                        temp_data  = temp_data.strip("\n") + "\t" + ''.join(line)+"\n"
                                        result_info.write(temp_data)
                                else:
                                    pass
                                 
                              
                            
                    # has 15 and 26
                    elif "|26" in line:
                        line = line.split("26")[-2].strip("|") #list
                        if "公司" in ''.join(line):
                            #print ''.join(self.common(''.join(line)))
                            #result_data.append(''.join(self.common(''.join(line))+"\n"))
                            temp_data  = temp_data.strip("\n") + "\t" + ''.join(self.common(''.join(line))+"\n")
                            result_info.write(temp_data)
                            #result_info.write(''.join(self.common(''.join(line))+"\n"))
                
                # only has 26 ----too messy.         
                elif "|26" in line:
                    if "公司" in ''.join(line):
                    #print ''.join(self.common(''.join(line)))
                    #result_data.append(''.join(self.common(''.join(line))+"\n"))
                        temp_data  = temp_data.strip("\n") + "\t" + ''.join(self.common(''.join(line))+"\n")
                        result_info.write(temp_data)
                
                # if 15 is at the end
                elif "15" in line:
                    if "15" in line.split("|")[-1]:                        
                        line = line.split("|15")[0]
                        line = unicode(line,"gbk")
                        temp = re.compile(u"[\u4e00-\u9fa5]{1}")
                        line = temp.findall(line)
                        for each_word in format_address:
                            each_word = unicode(each_word,"gbk")
                            temp_each_word = re.compile(u"[\u4e00-\u9fa5]{1}")
                            each_word = ''.join(temp_each_word.findall(each_word))                                        
                            if ''.join(line).rfind(each_word) is not -1:
                            #if ''.join(format_address).rfind(each_string) is not -1:                 
                            #line = ''.join(line)[''.join(line).rfind(each_string)+1:]
                                line = ''.join(line)[''.join(line).rfind(each_word)+len(each_word):]
                            else:
                                ine = ''.join(line)                        
                        #print "###" + ''.join(line)
                        #result_data.append(''.join(line)+"\n")
                        #result_info.write(''.join(line)+"\n")
                        temp_data  = temp_data.strip("\n") + "\t" + ''.join(line)+"\n"
                        result_info.write(temp_data)
                
                # in case there is data when there is not a 15 or 26
                else:
                    line = temp_data2
                    line = unicode(line,"gbk")
                    temp = re.compile(u"[\u4e00-\u9fa5]{1}")
                    line = temp.findall(line)
                    if "公司" in line:
                        #print "^^^"+''.join(self.common(''.join(line)))
                        #result_data.append(''.join(self.common(line))+"\n")
                        #result_info.write(''.join(self.common(''.join(line))+"\n"))
                        temp_data  = temp_data.strip("\n") + ''.join(self.common(''.join(line))+"\n")
                        result_info.write(temp_data)
                    
                result_info.flush()
                
            else:
                breaksasass

        #result_data = list(set(result_data))    
        #result_info.write(''.join(result_data))     
        file.close()
        result_info.close()
        
    def common(self,line):#str
        temp_line = line
        temp_line = unicode(temp_line,"gbk")
        temp = re.compile(u"[\u4e00-\u9fa5]{1}")
        temp_line = temp.findall(temp_line)
        #print ''.join(temp_line)
        if "公司" in ''.join(temp_line):
            line = line.split("公司")[0] + "公司"
            line = unicode(line,"gbk")
            temp = re.compile(u"[\u4e00-\u9fa5]{1}")
                    #print ''.join(temp)
            line = temp.findall(line)
            #print "***" + ''.join(line)
            #for each_string in line: #line is a list
            format_address
            for each_word in format_address:
                
                each_word = unicode(each_word,"gbk")
                temp_each_word = re.compile(u"[\u4e00-\u9fa5]{1}")
                each_word = ''.join(temp_each_word.findall(each_word))

                #print  "len"
                #print len(each_word)
                        #line = line.decode('utf-8')                    
                        #line = re_words.search(line, 0).group()                 
                       # print "each_string" + each_string
                   
                if ''.join(line).rfind(each_word) is not -1:
                #if ''.join(format_address).rfind(each_string) is not -1:
                    #print "index:"
                    #print ''.join(format_address).rfind(each_string)
                    line = ''.join(line)[''.join(line).rfind(each_word)+len(each_word):]

                else:
                    line = ''.join(line)
                #if each_string in format_mess:
                 #   line = line.strip(each_string)
            '''
            seg_list = jieba.cut(''.join(line),cut_all=False)
            for each_word in seg_list:
                print "seg_word:",each_word
                if ''.join(format_address).rfind(each_word) is not -1:
                    line = ''.join(seg_list)[''.join(seg_list).rfind(each_word)+1:]
                    print "seg_line" +line
                else:
                    pass
            '''       
        else:
            line = ''
        if len(line) <= 3:
            return ''
        else:
        #print "***" + ''.join(line)
            return line
    
    def uniq_data(self):
        data = open("EXTRACT_RESULT.txt",'r')
        contents = data.readlines()
        contents = list(set(contents))
        '''
        for each_line in contents:
            each_line = unicode(each_line,"gbk")
            temp = re.compile(u"[\u4e00-\u9fa5]{1}")
            each_line = temp.findall(each_line)
            if count(each_line) > 3:
                del each_line
        '''        
        new_data = open("SORTED_RESULT.txt",'w')
        new_data.write(''.join(contents))
        data.close()
        new_data.close()
        
'''result_log_info=open("EXTRACT_RESULT_LOG","w")
            cmd = "grep \'15\!\' line"  
            data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True) 
            result_log_info.write(data.stdout.read()) 
            result_log_info.close()'''
            
if __name__ == '__main__':
    test_object = COMPANY_EXTRACT()
    test_object.raw_extract()
    test_object.uniq_data()
