# -*- coding: utf-8 -*-
import os
file = open('/Users/lydia/projects/ttext.txt', 'r')

f = open('/Users/lydia/projects/header-img.sql', 'w')
for i in range(1, 20000):
    line = file.readline()
    print(line)
    string = line.split("	")
    print(string[0])
    print(string[1])
    sql = 'insert into public.users (user_nickname,created_time,updated_time,user_type,creator,updater,del_flag,profile_photo,user_uuid) values (\''+string[0]+'\',\'2019-07-09 14:59:22.118\',\'2019-07-09 14:59:22.118\',\'4\',0,0,0,\''+string[1]+'\',md5(\''+string[1]+'\'));'
    f.write(sql)
    f.write("\n")
print('success!')
f.close()



