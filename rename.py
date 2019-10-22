#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: ss

import os

def edit(path):
    t = os.listdir(path)
    for name in t:
        name = os.path.join(path,name)#获取文件的绝对路径，由于工作路径的原因，不能用os.path.abspath获取
        if name.endswith('.txt') and os.path.isfile(name):
            print('要修改的文件为{}'.format(name))
            os.rename(name,name+'.bak')#如果是文件重命名os.rename(src, dst)src -- 要修改的目录名 dst -- 修改后的目录名
        elif os.path.isdir(name):#如果是目录调用edit函数
            edit(name)
        else:
            print(name)

path = 'D:\\Python\\ss1\\02-练习\\002-5月\\测试\\'
edit(path)