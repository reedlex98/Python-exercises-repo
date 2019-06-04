
# -*- coding: utf-8 -*-

w = open('arq3.txt','w')
w.write(open('arq.txt').read())
print(w.read())