import requests
f=open('guizhou.txt','r')
headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
#response = requests.get(url,headers = headers)
#print((response.content).decode('utf-8'))
i=0
for url in f.readlines():
    i+=1
    print(i)
    response = requests.get(url,headers = headers)
    w=open(str(i)+'.html','w')
    w.write(((response.content).decode('utf-8')))
    w.close()
f.close()
