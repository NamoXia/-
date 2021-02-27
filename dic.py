'''
说明：用于单个姓名和生日组合生成密码字典，包含常见大小写组合
使用方式：直接运行，根据提示输入姓名和八位生日

'''
#!/usr/bin/python         
# -*- coding: UTF-8 -*-
# python3.7
# Author:Namo

from xpinyin import Pinyin
import os
#接收姓名和生日
def get_info():
    name = input("请输入中文姓名：")
    birth = input("请输入八位数字生日：")
    return name,birth

#生成拼音字典
def pinyin(name):
    p = Pinyin()
    name_pinyin = p.get_pinyin(name,'')   #获取全拼
    name_pinyin_cap = name_pinyin.upper() #全拼转为大写
    name_pinyin_init_cap = name_pinyin.capitalize() #全拼首字母大写
    
    name_init_pinyin = p.get_initials(name,'')       #获取首字母
    name_init_pinyin_low = name_init_pinyin.lower()  #首字母转小写
    name_init_pinyin_cap = name_init_pinyin_low.capitalize() #首字母的首字母大写

     #  将结果存储到列表中
    name_list = list()
    name_list.append(name_pinyin)
    name_list.append(name_pinyin_cap)
    name_list.append(name_pinyin_init_cap)
    name_list.append(name_init_pinyin)
    name_list.append(name_init_pinyin_low)
    name_list.append(name_init_pinyin_cap)
    return name_list

#生成生日字典
def numstr(birth):
    num_year = birth[0:4]
    num_monthday = birth[4:]
    num_front_six = birth[0:6]
    num_back_six = birth[2:]
    
    #  将结果存储到列表中
    num_list = list()
    num_list.append(num_year)
    num_list.append(num_monthday)
    num_list.append(num_front_six)
    num_list.append(num_back_six)
    return num_list

#将拼音和生日组合到一起，生成新字典
def link_name_num(name_list,num_list):
    link = list()
    for name in name_list:
        for num in num_list:
            link.append(name + num)
            link.append(num + name)
    return link

#将生成的数据存到文件dic.txt中
def save_dic(name_list,num_list,link_data):
    file = open('dic.txt','w')
    for name in name_list:
        file.write(name + '\n')
    for num in num_list:
        file.write(num + '\n')
    for data in link_data:
        file.write(data + '\n')
    file.close()
    
    print( "字典文件已保存至" + os.getcwd() +"\dic.txt")

#主程序
name,birth = get_info()
name_list=pinyin(name)   
num_list = numstr(birth)
link_list = link_name_num(name_list,num_list)
save_dic(name_list,num_list,link_list)





























