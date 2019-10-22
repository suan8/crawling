# -*- coding: utf-8 -*-
import os
f = open('/Users/lydia/projects/code.txt', 'w')
for i in range(29749, 30000):

    url = 'https://image.hualu.yetter.cn//app/user/avatar/{page}.jpg'.format(page=i)
    f.write(url)
    f.write("\n")
print('success!')
f.close()



