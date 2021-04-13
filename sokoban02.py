

import urllib.request

#url, на котором находится список преподователей
link = urllib.request.urlopen('http://sergkab.ru/web')

lines = []
for line in link.readlines():
    #
    #
    '''
    if line.find(b'<li>') != -1 and line.find(b'a href') != -1:
          lines.append(line)
    '''
    lines.append(line)
    #print (line)

link.close()
    
#Переводим bytes в str
for i in range(len(lines)):
    lines[i] = lines[i].decode('utf-8')
    print (lines[i])



'''

'''

